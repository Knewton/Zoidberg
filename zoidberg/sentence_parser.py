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
		self.operator = {}
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

	def track(self, val, attr, subtype=None, index=None, conv=False):
		if attr == "context":
			if subtype is not None:
				self.resolve_context(subtype, val)

		if attr == "comparator_context":
			if subtype is not None:
				conval = self.resolve_context(subtype, None, True)
				if conv:
					val = conval
				else:
					# Set the subtype for PRP comparator contexts
					val = (val, subtype)

		tup = (val, attr, subtype)
		if index is not None:
			self.parsed[index] = tup
		else:
			index = len(self.parsed)
			self.parsed.append(tup)
		self.track_longer(val)
		self.track_longer(attr)
		return index

	def resolve_context(self, subtype, val=None, compx=False):
		p = self.problem
		plurality, gender = subtype
		if val is not None:
			p.previous_contexts["plurality"][plurality] = \
				p.last_contexts["plurality"][plurality]
			p.previous_contexts["gender"][gender] = \
				p.last_contexts["gender"][gender]

			data = (val, subtype)
			p.last_contexts["plurality"][plurality] = data
			p.last_contexts["gender"][gender] = data
		else:
			if compx:
				plurality_c = p.previous_contexts["plurality"][plurality]
				gender_c = p.previous_contexts["gender"][gender]
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
		brain = self.problem.brain
		text = self.sentence_text

		if tag[:2] == "NN" or tag[:3] == "PRP": # Nouns and Pronouns
			return brain.noun_like(word, text)
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
		last_subtype = None
		last_conjunction = None
		phrasing_question = False
		subtype = None
		is_relative_quantity = False
		partial_context = None
		last_partial_context = None
		partial_subtype = None
		comparator_context = None
		main_context = None

		for s_tag in self.sentence:
			word, tag = s_tag
			did_something = False
			subtype = None
			if index == 0 and tag not in ["NNP", "NNPS"]:
				# Fix capitalization for non proper nouns
				word = word.lower()

			tag = p.brain.retag(word, tag)
			if tag == "!!!":
				print "Missing retag converter in the brain"
				exit(1)

			# Fix the parser as we go on brain retags
			def do_track(subtype):
				if subtype[0] is None and subtype[1] is None:
					subtype = None
					tag = p.brain.retag(word, tag)
					return False
				return True

			if tag in ["NN", "NNS"]:
				if last_tag in ["PRP$"]:
					# Detects Jane's friends; probably context
					context = " ".join([partial_context, word])
					self.parsed.pop()
					self.contexts.append(context)
					did_something = True
					subtype = self.get_subtype(word, tag)

					partial_context = None
					last_partial_context = None
					partial_subtype = None

					if do_track(subtype):
						if subtype[0] == "plural" and subtype[1] == "mixed":
							# PRP$ will always have a noun like last_subtype
							last_plural, last_gender = last_subtype
							# Last Plural Context
							lpc = p.last_contexts["plurality"][last_plural]
							# Last Gender Context
							lgc = p.last_contexts["gender"][last_gender]

							last_context = None
							if lgc == lpc:
								last_context = lgc
							elif lgc is not None:
								last_context = lgc
							elif lpc is not None:
								last_context = lpc

							if last_context is not None:
								# Last context string
								inc = p.brain.inclusive(word,
									"'{0}' ({1}) in '{2}'".format(last_word,
															last_context[0],
															context))
								# Add the context by the word for easier lookup
								# this will capture 'her friends' and define
								# the concept of inclusiveness for friends then
								# later auto-apply this to the concept of say,
								# 'his friends'
								p.brain.add("inclusive", context, inc)
						# Assume the first context after a comparison is the
						# comparator context
						if is_relative_quantity and not comparator_context and main_context:
							comparator_context = context
							self.track(context, "comparator_context", subtype, conv=True)
						else:
							main_context = context
							self.track(context, "context", subtype)
				else:
					if last_conjunction is not None:
						conjunction = (word, last_conjunction)
						self.conjunctions.append(conjunction)
						did_something = True
						self.track(conjunction, "subordinate", subtype)
					else:
						subtype = self.get_subtype(word, tag)
						if do_track(subtype):
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

			if tag == "SUB":
				did_something = True
				self.track(word, "subordinate", subtype)

			if tag == "PRP":
				c = self.resolve_context(subtype)
				if c is not None:
					did_something = True
					if is_relative_quantity and not comparator_context and main_context:
						comparator_context = c[0]
						self.track(c[0], "comparator_context", subtype, conv=True)
					else:
						main_context = c[0]
						self.track(c[0], "context", subtype)

			if tag == "PRP$":
				if last_conjunction is not None:
					if is_relative_quantity and not comparator_context and main_context:
						did_something = True
						comparator_context = word
						self.track(word, "comparator_context", subtype, conv=True)
						last_conjunction = None

				if not did_something:
					did_something = True
					partial_context = word
					partial_subtype = subtype
					last_partial_context = self.track(word, "partial_context",
							subtype)

			if tag in ["NNP", "NNPS"]:
				if last_tag in ["NNP", "NNPS"]:
					# Last was partial context; the "Mrs." in "Mrs. Jones"
					lc = self.contexts.pop()
					self.parsed.pop()

					context = " ".join([last_word, word])
					if is_relative_quantity and comparator_context == lc:
						comparator_context = context
					if subtype is not None and subtype[1] == "ambiguous":
						old = self.get_subtype(last_word, last_tag)
						subtype = (subtype[0], old[1])
				else:
					context = word
				self.contexts.append(context)
				did_something = True
				if is_relative_quantity and not comparator_context and main_context:
					comparator_context = context
					self.track(context, "comparator_context", subtype)
				else:
					main_context = context
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
					subtype = self.get_subtype(word, tag)
					self.track(word, "operator", subtype)
				else:
					did_something = True
					gtype = p.brain.gerund(word, self.sentence_text)
					self.track(word, gtype, subtype)

			if tag == "JJR":
				did_something = True
				adj = p.brain.relative(word, self.sentence_text)
				is_relative_quantity = adj != "noise"
				self.track(word, adj, subtype)

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
				dtype = p.brain.determiner(word, self.sentence_text)
				self.track(word, dtype, subtype)

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
			last_subtype = subtype
			index += 1

		if partial_context:
			context = partial_context
			idx = last_partial_context
			stype = partial_subtype

			partial_context = None
			last_partial_context = None
			partial_subtype = None

			if is_relative_quantity and not comparator_context and main_context:
				comparator_context = context
				self.track(context, "comparator_context", stype, idx, True)

		# Make all the inferred items unique
		self.raw_operators = uniq(self.raw_operators)
		self.contexts = uniq(self.contexts)
		self.units = uniq(self.units)

		# Resolve the verbs to actual operators using the brain
		for o in self.raw_operators:
			op = p.brain.operator(o, self.sentence_text)
			self.operators.append(op)
			self.operator[o] = op
		self.operators = uniq(self.operators)

		text = self.sentence_text

		# Resolve the subordinates
		for o in self.conjunctions:
			subordinate, conjunction = o
			self.subordinates.append(
				(subordinate, p.brain.subordinate(subordinate, text)))
		self.subordinates = uniq(self.subordinates)

	def __str__(self):
		return self.sentence_text

