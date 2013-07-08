#!/usr/bin/env python

from utilities import uniq

class SentenceParser(object):
	def __init__(self, sentence, problem, text):
		self.index = 0
		self.acting = False
		self.last_operator = None
		self.last_operator_type = None
		self.last_word = None
		self.last_tag = None
		self.last_unit = None
		self.last_unit_tag = None
		self.last_unit_index = None
		self.last_verb_tag = None
		self.last_verb = -1
		self.last_noun_tag = None
		self.last_subtype = None
		self.last_conjunction = None
		self.conjunction_parts = []
		self.phrasing_question = False
		self.subtype = None
		self.is_relative_quantity = False
		self.partial_context = None
		self.last_partial_context = None
		self.partial_subtype = None
		self.comparator_context = None
		self.main_context = None
		self.last_context = None
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

		# Actions are like a joint structure of contexts and units
		# in that a context can "own" an action the same way it can
		# own a unit. The action also acts as a "subcontext" as the
		# context owner (in this case, actor) can be "performing" an
		# action which differentiates it from the larger context.
		self.actions = []

		# Subordinate conjunctions; time/place/cause and effect which can
		# identify the time period
		self.conjunctions = []
		self.subordinates = []
		self.subordinate_strings = {}

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

		def process(word, tag):
			did_something = False
			self.subtype = None
			if self.index == 0 and tag not in ["NNP", "NNPS"]:
				# Fix capitalization for non proper nouns
				word = word.lower()

			word, tag = p.brain.retag(word, tag)
			if tag == "!!!":
				print "Missing retag converter in the brain"
				exit(1)

			if self.last_conjunction is not None:
				self.conjunction_parts.append(word)

			# Fix the parser as we go on brain retags
			def do_track(subtype, tag):
				if subtype[0] is None and subtype[1] is None:
					subtype = None
					tag = p.brain.retag(word, tag)
					return (False, subtype, tag)
				return (True, subtype, tag)

			if tag in ["NN", "NNS"]:
				if self.last_tag in ["PRP$"]:
					# Detects Jane's friends; probably context
					context = " ".join([self.partial_context, word])
					self.parsed.pop()
					self.last_context = context
					self.contexts.append(context)
					did_something = True
					self.subtype = self.get_subtype(word, tag)

					self.partial_context = None
					self.last_partial_context = None
					self.partial_subtype = None

					track, self.subtype, tag = do_track(self.subtype, tag)

					if track:
						if self.subtype[0] == "plural" and self.subtype[1] == "mixed":
							# PRP$ will always have a noun like last_subtype
							last_plural, last_gender = self.last_subtype
							# Last Plural Context
							lpc = p.last_contexts["plurality"][last_plural]
							# Last Gender Context
							lgc = p.last_contexts["gender"][last_gender]

							self.last_context = None
							if lgc == lpc:
								self.last_context = lgc
							elif lgc is not None:
								self.last_context = lgc
							elif lpc is not None:
								self.last_context = lpc

							if self.last_context is not None:
								# Last context string
								inc = p.brain.inclusive(word,
									"'{0}' ({1}) in '{2}'".format(self.last_word,
															self.last_context[0],
															context))
								# Add the context by the word for easier lookup
								# this will capture 'her friends' and define
								# the concept of inclusiveness for friends then
								# later auto-apply this to the concept of say,
								# 'his friends'
								p.brain.add("inclusive", context, inc)
						# Assume the first context after a comparison is the
						# comparator context
						if self.is_relative_quantity and not self.comparator_context and self.main_context:
							self.comparator_context = context
							self.track(context, "comparator_context", self.subtype, conv=True)
						else:
							self.main_context = context
							self.track(context, "context", self.subtype)
				else:
					if self.last_conjunction is not None:
						conjunction = (word, self.last_conjunction)
						self.last_conjunction = None
						self.subordinate_strings[word] = " ".join(self.conjunction_parts)
						self.conjunction_parts = []
						self.conjunctions.append(conjunction)
						did_something = True
						self.track(conjunction, "subordinate", self.subtype)
					else:
						self.subtype = self.get_subtype(word, tag)
						track, self.subtype, tag = do_track(self.subtype, tag)
						did_something = True
						if track:
							unit = word
							if tag == "NNS" and self.last_tag == "NN":
								unit = " ".join([self.last_word, word])
								self.units.pop()
								self.parsed.pop()

							if not unit in p.units_acting_as_context or not p.units_acting_as_context[unit]:
								self.last_unit = unit
								self.last_unit_tag = tag
								self.last_unit_index = len(self.parsed)
								self.units.append(unit)
								self.track(unit, "unit", self.subtype)
							else:
								context = unit
								# @TODO: This needs to be a subroutine or something
								self.last_context = context
								self.contexts.append(context)
								if self.is_relative_quantity and not self.comparator_context and self.main_context:
									self.comparator_context = context
									self.track(context, "comparator_context", self.subtype)
								else:
									self.main_context = context
									self.track(context, "context", self.subtype)

			if not did_something and self.subtype == None:
				self.subtype = self.get_subtype(word, tag)

			if tag == "SUB":
				did_something = True
				self.track(word, "subordinate", self.subtype)

			if tag == "PRP":
				c = self.resolve_context(self.subtype)
				if c is not None:
					# If we're setting a relative quantity and the contexts are
					# the same we're not actually setting a relative quantity
					# we are simply indicating a mathematical operand
					if self.is_relative_quantity and c[0] == self.last_context:
						self.is_relative_quantity = False
					did_something = True
					if self.is_relative_quantity and not self.comparator_context and self.main_context:
						self.comparator_context = c[0]
						self.track(c[0], "comparator_context", self.subtype, conv=True)
					else:
						self.main_context = c[0]
						self.track(c[0], "context", self.subtype)

			if tag == "PRP$":
				if self.last_conjunction is not None:
					if self.is_relative_quantity and not self.comparator_context and self.main_context:
						did_something = True
						self.comparator_context = word
						self.track(word, "comparator_context", self.subtype, conv=True)
						self.last_conjunction = None
						self.conjunction_parts = []

				if not did_something:
					did_something = True
					self.partial_context = word
					self.partial_subtype = self.subtype
					self.last_partial_context = self.track(word, "partial_context",
							self.subtype)

			if tag in ["NNP", "NNPS"]:
				if self.last_tag in ["NNP", "NNPS"]:
					# Last was partial context; the "Mrs." in "Mrs. Jones"
					self.last_context = None
					lc = self.contexts.pop()
					self.parsed.pop()

					context = " ".join([self.last_word, word])
					if self.is_relative_quantity and self.comparator_context == lc:
						self.comparator_context = context
					if self.subtype is not None and self.subtype[1] == "ambiguous":
						old = self.get_subtype(self.last_word, self.last_tag)
						self.subtype = (self.subtype[0], old[1])
				else:
					context = word
				self.last_context = context
				self.contexts.append(context)
				did_something = True
				if self.is_relative_quantity and not self.comparator_context and self.main_context:
					self.comparator_context = context
					self.track(context, "comparator_context", self.subtype)
				else:
					self.main_context = context
					self.track(context, "context", self.subtype)

			if tag[:2] == "VB":
				if tag == "VB":
					if self.last_verb_tag is not None:
						# VB*...VB indicates a question not an operation
						self.last_operator = None
						q_start = self.raw_operators.pop()
						self.track(q_start, "q_start", self.subtype, self.last_verb)
						did_something = True
						self.track(word, "q_stop", self.subtype)
				elif tag != "VBG":
					self.last_verb_tag = tag
					self.last_verb = len(self.parsed)
					self.last_operator = word
					self.raw_operators.append(word)
					did_something = True
					self.subtype = self.get_subtype(word, tag)
					self.track(word, "operator", self.subtype)
				else:
					did_something = True
					gtype = p.brain.gerund(word, self.sentence_text)
					if gtype == "acting":
						self.acting = False
						self.actions.append(word)
					self.track(word, gtype, self.subtype)

			if tag == "JJR":
				did_something = True
				adj = p.brain.relative(word, self.sentence_text)
				self.is_relative_quantity = adj != "noise"
				self.track(word, adj, self.subtype)

			if tag == "IN":
				self.last_conjunction = word
				self.conjunction_parts.append(word)
				did_something = True
				self.track(word, "conjunction", self.subtype)

			if tag == ".":
				did_something = True
				self.track(word, "punctuation", self.subtype)

			if tag == "CD": # A cardinal number
				did_something = True
				self.track(word, "constant", self.subtype)

			if tag == "DT": # A determiner (the)
				did_something = True
				dtype = p.brain.determiner(word, self.sentence_text)
				self.track(word, dtype, self.subtype)

			if tag == "RB": # An adverb, probably a subordinate?
				if self.last_conjunction is not None:
					conjunction = (word, self.last_conjunction)
					self.last_conjunction = None
					self.subordinate_strings[word] = " ".join(self.conjunction_parts)
					self.conjunction_parts = []
				else:
					conjunction = (word, None)
					self.subordinate_strings[word] = word
				self.conjunctions.append(conjunction)
				did_something = True
				self.track(conjunction, "subordinate", self.subtype)

			# Anything about phrasing must come before the wh-determiner block
			if tag == "JJ": # Adjective
				if self.phrasing_question:
					self.parsed.pop()
					did_something = True
					self.track(" ".join([self.last_word, word]), "asking", self.subtype)

			if tag == "PIP":
				did_something = True
				self.track(word, "pre_ind_plu", self.subtype)
				self.acting = True
				if self.last_unit is not None and self.last_context is None:
					# If we have a present indicitive plural with no context
					# it is likely that we're dealing with a context which has
					# been misinterpreted as a unit, so switch that
					# mistake here.
					p.units_acting_as_context[self.last_unit] = True

					# Remove the last unit and make it a context
					context = self.units.pop()
					self.last_context = context
					self.contexts.append(context)
					if self.is_relative_quantity and not self.comparator_context and self.main_context:
						self.comparator_context = context
						self.track(context, "comparator_context", self.subtype, self.last_unit_index)
					else:
						self.main_context = context
						self.track(context, "context", self.subtype, self.last_unit_index)

					# @TODO: This needs a much better tracking system
					self.last_unit = None
					self.last_unit_tag = None
					self.last_unit_index = -1

			if tag in ["WRB", "WDT", "WP", "WP$"]: # Wh- determiner
				self.question = True
				self.phrasing_question = True
				did_something = True
				self.track(word, "asking", self.subtype)
			elif self.phrasing_question:
				self.phrasing_question = False

			if self.subtype is not None:
				did_something = True

			if not did_something:
				p.brain.unknown(word, tag, self.subtype, self.sentence_text)
				process(word, tag)

			self.last_word = word
			self.last_tag = tag
			self.last_subtype = self.subtype

		for s_tag in self.sentence:
			process(*s_tag)
			self.index += 1

		if self.partial_context:
			context = self.partial_context
			idx = self.last_partial_context
			stype = self.partial_subtype

			self.partial_context = None
			self.last_partial_context = None
			self.partial_subtype = None

			if self.is_relative_quantity and not self.comparator_context and self.main_context:
				self.comparator_context = context
				self.track(context, "comparator_context", stype, idx, True)

		# Make all the inferred items unique
		self.raw_operators = uniq(self.raw_operators)
		self.contexts = uniq(self.contexts)
		self.units = uniq(self.units)
		self.actions = uniq(self.actions)

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

