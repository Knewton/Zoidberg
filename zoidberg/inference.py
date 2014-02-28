#!/usr/bin/env python
from utilities import list_format, uniq, output_tuples
from sentence_parser import SentenceParser

OPERATOR_STR = {
	"single_context": {
		"eq": "having",
		"ad": "getting",
		"mu": "getting",
		"su": "losing",
		"di": "losing"
	},
	"multiple_contexts": {
		"eq": "grouping",
		"ad": "comparing or exchanging",
		"mu": "comparing or exchanging",
		"su": "comparing or exchanging",
		"di": "comparing or exchanging"
	},
	"no_context": {
		"eq": "some",
		"ad": "increased",
		"mu": "increased",
		"su": "decreased",
		"di": "decreased"
	},
	"context_actions_nounit": {
		"eq": "the number of",
		"ad": "an increasing number of",
		"mu": "an increasing number of",
		"su": "a decreasing number of",
		"di": "a decreasing number of"
	}
}

class Inference(object):
	def __init__(self, problem):
		# The parsed sentences used for making inferences
		self.sentences = []
		self.longest_phrase = None

		# The sentences which are questions
		self.queries = []

		# Collection of verbs which describe data manipulations
		self.preops = []
		self.operators = []

		# Contexts are the way to define the "Joe" of "Joe's apples"
		self.contexts = []

		# Units are the way to define the "apple" of "Joe's apples"
		self.units = []

		# Actions are a way to subsect contexts
		self.actions = []

		# Subordinate conjunctions; time/place/cause and effect which can
		# identify the time period
		self.subordinates = []

		# Display strings for subordinates
		self.subordinate_strings = {}

		# Store a reference to the problem
		self.problem = problem

		# Is the problem about needing something?
		self.is_requirement_problem = False

		# Execute
		self.execute()

	def possible_query(self, index):
		if not index in self.possible_queries:
			self.possible_queries[index] = 1
		else:
			self.possible_queries[index] += 1

	def track_longer(self, l):
		if self.longest_phrase is None or self.longest_phrase < l:
			self.longest_phrase = l

	def execute(self):
		p = self.problem
		raw_actions, raw_operators, raw_subordinates = [], [], []
		index = 0

		for s_tags in p.sentence_tags:
			s = SentenceParser(s_tags, p, p.sentences[index])
			self.sentences.append(s)
			self.track_longer(s.longest_phrase)

			if s.is_about_requirements:
				self.is_requirement_problem = True

			raw_operators += s.operators
			raw_actions += s.actions
			raw_subordinates += s.subordinates

			self.contexts += s.contexts
			self.units += s.units
			if len(s.subordinate_strings) > 0:
				sd = dict(s.subordinate_strings)
				if len(self.subordinate_strings) > 0:
					sd.update(self.subordinate_strings)
				self.subordinate_strings = sd

			if s.question:
				self.queries.append(index)

			index += 1

		# Ensure uniqueness in our data
		raw_operators = uniq(raw_operators)
		raw_actions = uniq(raw_actions)
		raw_subordinates = uniq(raw_subordinates)

		self.contexts = uniq(self.contexts)
		self.units = uniq(self.units)

		self.condense()

		# Set our phrasings based on the contexts in play
		if len(self.contexts) > 1:
			op_key = OPERATOR_STR["multiple_contexts"]
		elif len(self.contexts) > 0:
			op_key = OPERATOR_STR["single_context"]
		else:
			op_key = OPERATOR_STR["no_context"]

		for sub in raw_subordinates:
			word, subtype = sub
			if subtype is not None and subtype[0:4] != "time":
				if "grouping" not in subtype:
					self.subordinates.append(self.subordinate_strings[word])
		self.subordinates = uniq(self.subordinates)

		format_operators = True
		for act in raw_actions:
			self.actions.append(act)
		self.actions = uniq(self.actions)

		pre_ops = False
		if len(self.units) == 0 and len(self.actions) > 0:
			pre_ops = True
			# We have special phrasing which is mucked up by the operators
			# if we're only dealing with
			op_key = OPERATOR_STR["context_actions_nounit"]

		for op in raw_operators:
			if op != "eq" or len(raw_operators) == 1:
				try:
					self.operators.append(op_key[op])
				except:
					pass
		self.operators = uniq(self.operators)

		if pre_ops:
			self.preops = self.operators
			self.operators = []

	def __str__(self):
		o = []
		i = ["I think this problem is about"]
		thought_any = False

		multiple_contexts = len(self.contexts) > 1
		for x in [self.preops, self.contexts, self.operators, self.actions,
					self.units, self.subordinates]:
			f = list_format(x)
			if f is not None:
				thought_any = True
				i.append(f)

		if len(self.queries) == 1:
			i.append("and asks a single question")
		elif len(self.queries) > 1:
			i.append("and asks multiple questions")
		else:
			i.append("however, I don't know what it wants for an answer")

		o.append("## Problem inference")
		if thought_any:
			o.append("    " + " ".join(i) + ".")
		else:
			o.append("    I have literally no idea what's going on here.")

		o.append("\n## Parsed problem")
		output_tuples(self.sentences, o, self.longest_phrase, self.problem.brain)

		return "\n".join(o)

	def condense(self):
		self.contexts = self.problem.brain.condense(self.contexts)
		self.units = self.problem.brain.condense(self.units)

