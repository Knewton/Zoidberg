#!/usr/bin/env python

from utilities import uniq

class SentenceParser(object):
	def __init__(self, sentence, problem, text):
		self.sentence = sentence
		self.problem = problem
		self.sentence_text = text
		self.question = False
		self.longest_phrase = None

		# The parsed sentence of chunked components
		self.parsed = []

		# Collection of verbs which describe data manipulations
		self.operators = []
		self.raw_operators = []

		# Contexts are the way to define the "Joe" of "Joe's apples"
		self.contexts = []

		# Units are the way to define the "apple" of "Joe's apples"
		self.units = []

		# Subordinate conjunctions; time/place/cause and effect which can
		# identify the time period
		self.conjunctions = []
		self.subordinates = []

		self.execute()

	def track_longer(self, v):
		l = len(v)
		if self.longest_phrase is None or self.longest_phrase < l:
			self.longest_phrase = l

	def track(self, val, attr, subtype=None, index=None):
		if attr == "context":
			if subtype is not None:
				self.resolve_context(subtype, val)
		tup = (val, attr, subtype)
		if index is not None:
			self.parsed[index] = tup
		else:
			self.parsed.append(tup)
		self.track_longer(val)
		self.track_longer(attr)

	def resolve_context(self, subtype, val=None):
		p = self.problem
		plurality, gender = subtype
		if val is not None:
			data = (val, subtype)
			p.last_contexts["plurality"][plurality] = data
			p.last_contexts["gender"][gender] = data
		else:
			plurality_c = p.last_contexts["plurality"][plurality]
			gender_c = p.last_contexts["gender"][gender]

			if plurality_c is not None and gender_c is not None:
				if (plurality_c[0] == gender_c[0] or
					gender == "mixed" and plurality == "multiple" or
					plurality == "multiple"):
					return plurality_c
				else:
					return gender_c
			elif plurality_c is not None:
				return plurality_c
			elif gender_c is not None:
				return gender_c
		return None

	def __iter__(self):
			return iter(self.parsed)

	def get_subtype(self, word, tag):
		if tag[:2] == "NN": # Nouns
			return self.problem.brain.noun_like(word, self.sentence_text)
		elif tag[:3] == "PRP": # Pronouns
			return self.problem.brain.noun_like(word, self.sentence_text)
		else:
			return None

	def execute(self):
		p = self.problem
		index = 0

		last_word = None
		last_tag = None
		last_verb_tag = None
		last_verb = -1
		last_noun_tag = None
		last_conjunction = None
		phrasing_question = False
		subtype = None

		for s_tag in self.sentence:
			word, tag = s_tag
			did_something = False
			subtype = None
			if index == 0 and tag not in ["NNP", "NNPS"]:
				# Fix capitalization for non proper nouns
				word = word.lower()

			if tag in ["NN", "NNS"]:
				if last_tag in ["PRP$"]:
					# Detects Jane's friends; probably context
					context = " ".join([last_word, word])
					self.parsed.pop()
					self.contexts.append(context)
					did_something = True
					subtype = self.get_subtype(word, tag)
					self.track(context, "context", subtype)
				else:
					if last_conjunction is not None:
						conjunction = (word, last_conjunction)
						self.conjunctions.append(conjunction)
						did_something = True
						self.track(conjunction, "subordinate", subtype)
					else:
						subtype = self.get_subtype(word, tag)
						unit = word
						if tag == "NNS" and last_tag == "NN":
							unit = " ".join([last_word, word])
							self.units.pop()
							self.parsed.pop()
						self.units.append(unit)
						did_something = True
						self.track(unit, "unit", subtype)

			if not did_something and subtype == None:
				subtype = self.get_subtype(word, tag)

			if tag == "PRP":
				c = self.resolve_context(subtype)
				if c is not None:
					did_something = True
					self.track(c[0], "context", subtype)

			if tag in ["NNP", "NNPS"]:
				if last_tag in ["NNP", "NNPS"]:
					# Last was partial context; the "Mrs." in "Mrs. Jones"
					self.contexts.pop()
					self.parsed.pop()

					context = " ".join([last_word, word])
					if subtype is not None and subtype[1] == "ambiguous":
						old = self.get_subtype(last_word, last_tag)
						subtype = (subtype[0], old[1])
				else:
					context = word
				self.contexts.append(context)
				did_something = True
				self.track(context, "context", subtype)

			if tag[:2] == "VB":
				if tag == "VB":
					if last_verb_tag is not None:
						# VB*...VB indicates a question not an operation
						q_start = self.raw_operators.pop()
						self.track(q_start, "q_start", subtype, last_verb)
						did_something = True
						self.track(word, "q_stop", subtype)
				elif tag != "VBG":
					last_verb_tag = tag
					last_verb = len(self.parsed)
					self.raw_operators.append(word)
					did_something = True
					self.track(word, "operator", subtype)

			if tag == "IN":
				last_conjunction = word
				did_something = True
				self.track(word, "conjunction", subtype)

			if tag == ".":
				did_something = True
				self.track(word, "punctuation", subtype)

			if tag == "CD": # A cardinal number
				did_something = True
				self.track(word, "constant", subtype)

			if tag == "DT": # A determiner (the)
				did_something = True
				self.track(word, "noise", subtype)

			if tag == "RB": # An adverb, probably a subordinate?
				if last_conjunction is not None:
					conjunction = (word, last_conjunction)
				else:
					conjunction = (word, None)
				self.conjunctions.append(conjunction)
				did_something = True
				self.track(conjunction, "subordinate", subtype)

			# Anything about phrasing must come before the wh-determiner block
			if tag == "JJ": # Adjective
				if phrasing_question:
					self.parsed.pop()
					did_something = True
					self.track(" ".join([last_word, word]), "asking", subtype)

			if tag in ["WRB", "WDT", "WP", "WP$"]: # Wh- determiner
				self.question = True
				phrasing_question = True
				did_something = True
				self.track(word, "asking", subtype)
			elif phrasing_question:
				phrasing_question = False

			if not did_something:
				self.track((word, tag), "unknown", subtype)

			last_word = word
			last_tag = tag
			index += 1

		# Make all the inferred items unique
		self.raw_operators = uniq(self.raw_operators)
		self.contexts = uniq(self.contexts)
		self.units = uniq(self.units)

		text = self.sentence_text

		# Resolve the verbs to actual operators using the brain
		for o in self.raw_operators:
			self.operators.append(p.brain.operator(o, text))
		self.operators = uniq(self.operators)

		# Resolve the subordinates
		for o in self.conjunctions:
			subordinate, conjunction = o
			self.subordinates.append(
				(subordinate, p.brain.subordinate(subordinate, text)))
		self.subordinates = uniq(self.subordinates)

	def __str__(self):
		return self.sentence_text

