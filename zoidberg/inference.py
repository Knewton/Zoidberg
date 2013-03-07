#!/usr/bin/env python
from utilities import list_format
from sentence_parser import SentenceParser

OPERATOR_STR = {
	"multiple_contexts": {
		"eq": "having",
		"ad": "exchanging",
		"mu": "exchanging",
		"su": "exchanging",
		"di": "exchanging"
	},
	"single_context": {
		"eq": "having",
		"ad": "getting",
		"mu": "getting",
		"su": "losing",
		"di": "losing"
	},
	"no_context": {
		"eq": "some",
		"ad": "increased",
		"mu": "increased",
		"su": "decreased",
		"di": "decreased"
	}
}

class Inference(object):
	def __init__(self, problem):
		# The parsed sentences used for making inferences
		self.sentences = []

		# The sentences which are questions
		self.queries = []

		# Collection of verbs which describe data manipulations
		self.operators = []

		# Contexts are the way to define the "Joe" of "Joe's apples"
		self.contexts = []

		# Units are the way to define the "apple" of "Joe's apples"
		self.units = []

		# Subordinate conjunctions; time/place/cause and effect which can
		# identify the time period
		self.subordinates = []

		# Store a reference to the problem
		self.problem = problem

		# Execute
		self.execute()

	def possible_query(self, index):
		if not index in self.possible_queries:
			self.possible_queries[index] = 1
		else:
			self.possible_queries[index] += 1

	def execute(self):
		p = self.problem
		raw_operators = []
		index = 0

		for s_tags in p.sentence_tags:
			s = SentenceParser(s_tags, p, p.sentences[index])
			self.sentences.append(s)

			raw_operators += s.operators
			self.contexts += s.contexts
			self.units += s.units
			self.subordinates += s.subordinates

			if s.question:
				self.queries.append(index)

			index += 1

		# Ensure uniqueness in our data
		raw_operators = list(set(raw_operators))
		self.contexts = list(set(self.contexts))
		self.units = list(set(self.units))
		self.subordinates = list(set(self.subordinates))

		if len(self.contexts) > 1:
			op_key = OPERATOR_STR["multiple_contexts"]
		elif len(self.contexts) > 0:
			op_key = OPERATOR_STR["single_context"]
		else:
			op_key = OPERATOR_STR["no_context"]

		# Resolve the verbs to actual operators using the brain
		for op in raw_operators:
			if op != "eq" or len(raw_operators) == 1:
				self.operators.append(op_key[op])
		self.operators = list(set(self.operators))

	def __str__(self):
		o = []
		i = ["I think this problem is about"]
		thought_any = False

		multiple_contexts = len(self.contexts) > 1
		for x in [self.contexts, self.operators, self.units]:
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
			o.append(" ".join(i) + ".")
		else:
			o.append("I have literally no idea what's going on here.")

		o.append("\n## Parsed problem")
		self.problem.tag_print(self.sentences, o)

		return "\n".join(o)
