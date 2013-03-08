#!/usr/bin/env python

class SentenceParser(object):
	def __init__(self, sentence, problem, text):
		self.sentence = sentence
		self.problem = problem
		self.sentence_text = text
		self.question = False

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

	def track(self, val, attr):
		self.parsed.append((val, attr))

	def __iter__(self):
			return iter(self.parsed)

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

		for s_tag in self.sentence:
			word, tag = s_tag
			did_something = False
			if index == 0 and tag not in ["NNP", "NNPS"]:
				# Fix capitalization for non proper nouns
				word = word.lower()

			if tag == "PRP":
				if p.last_context is not None:
					did_something = True
					self.track(p.last_context, "context")

			if tag in ["NN", "NNS"]:
				if last_tag in ["PRP$"]:
					# Detects Jane's friends; probably context
					context = " ".join([last_word, word])
					p.last_context = context
					self.contexts.append(context)
					did_something = True
					self.track(context, "context")
				else:
					if last_conjunction is not None:
						conjunction = (last_conjunction, word)
						self.conjunctions.append(conjunction)
						did_something = True
						self.track(conjunction, "subordinate")
					else:
						unit = word
						if tag == "NNS" and last_tag == "NN":
							unit = " ".join([last_word, word])
							self.units.pop()
							self.parsed.pop()
						self.units.append(unit)
						did_something = True
						self.track(unit, "unit")

			if tag in ["NNP", "NNPS"]:
				if last_tag in ["NNP", "NNPS"]:
					# Last was partial context; the "Mrs." in "Mrs. Jones"
					self.contexts.pop()
					self.parsed.pop()

					context = " ".join([last_word, word])
				else:
					context = word
				p.last_context = context
				self.contexts.append(context)
				did_something = True
				self.track(context, "context")

			if tag[:2] == "VB":
				if tag == "VB":
					if last_verb_tag is not None:
						# VB*...VB indicates a question not an operation
						q_start = self.raw_operators.pop()
						self.parsed[last_verb] = (q_start, "q_start")
						did_something = True
						self.track(word, "q_stop")
				elif tag != "VBG":
					last_verb_tag = tag
					last_verb = index - 1
					self.raw_operators.append(word)
					did_something = True
					self.track(word, "operator")

			if tag == "IN":
				last_conjunction = word
				did_something = True
				self.track(word, "conjunction")

			if tag == ".":
				did_something = True
				self.track(word, "punctuation")

			if tag == "CD": # A cardinal number
				did_something = True
				self.track(word, "constant")

			if tag == "DT": # A determiner (the)
				did_something = True
				self.track(word, "noise")

			if tag == "RB": # An adverb, probably a subordinate?
				if last_conjunction is not None:
					conjunction = (last_conjunction, word)
				else:
					conjunction = (None, word)
				self.conjunctions.append(conjunction)
				did_something = True
				self.track(conjunction, "subordinate")

			# Anything about phrasing must come before the wh-determiner block
			if tag == "JJ": # Adjective
				if phrasing_question:
					self.parsed.pop()
					did_something = True
					self.track(" ".join([last_word, word]), "asking")

			if tag in ["WRB", "WDT", "WP", "WP$"]: # Wh- determiner
				self.question = True
				phrasing_question = True
				did_something = True
				self.track(word, "asking")
			elif phrasing_question:
				phrasing_question = False

			if not did_something:
				self.track((word, tag), ("unknown"))

			last_word = word
			last_tag = tag
			index += 1

		# Make all the inferred items unique
		self.raw_operators = list(set(self.raw_operators))
		self.contexts = list(set(self.contexts))
		self.units = list(set(self.units))

		text = self.sentence_text

		# Resolve the verbs to actual operators using the brain
		for o in self.raw_operators:
			self.operators.append(p.brain.operator(o, text))
		self.operators = list(set(self.operators))

		# Resolve the subordinates
		for o in self.conjunctions:
			conjunction, subordinate = o
			self.subordinates.append(p.brain.subordinate(subordinate, text))
		self.subordinates = list(set(self.subordinates))

	def __str__(self):
		return self.sentence_text

