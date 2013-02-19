#!/usr/bin/env python
from utilities import list_format

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
		# Query guess; accumulate points to determine what sentence is question
		self.possible_queries = {}
		self.query_points = {
			"question_mark": [],
			"verb_form": []
		}

		# Store a reference to the problem
		self.problem = problem

		# Execute
		self._execute()

	def _possible_query(self, index):
		if not index in self.possible_queries:
			self.possible_queries[index] = 1
		else:
			self.possible_queries[index] += 1

	def _execute(self):
		p = self.problem
		last_word, last_tag = None, None
		last_verb_tag = None
		index = 0

		for s_tags in p.sentence_tags:
			last_verb_tag = None
			last_conjunction = None
			s_index = 0

			for s_tag in s_tags:
				word, tag = s_tag

				if s_index == 0 and tag not in ["NNP", "NNPS"]:
					# Fix capitalization for non proper nouns
					word = word.lower()

				if tag in ["NN", "NNS"]:
					if last_tag in ["PRP$"]:
						# Detects Jane's friends; probably context
						self.contexts.append(" ".join([last_word, word]))
					else:
						if last_conjunction is not None:
							self.conjunctions.append((last_conjunction, word))
						elif tag == "NNS":
							self.units.append(word)

				if tag in ["NNP", "NNPS"]:
					if last_tag in ["NNP", "NNPS"]:
						# Last was partial context; the "Mrs." in "Mrs. Jones"
						self.contexts.pop()
						self.contexts.append(" ".join([last_word, word]))
					else:
						self.contexts.append(word)

				if tag[:2] == "VB":
					if tag == "VB":
						if last_verb_tag is not None:
							# VB*...VB indicates a question not an operation
							self.raw_operators.pop()
							self.query_points["verb_form"].append(index)
					elif tag != "VBG":
						last_verb_tag = tag
						self.raw_operators.append(word)

				if tag == "IN":
					last_conjunction = word

				if tag == "." and word == "?":
					self.query_points["question_mark"].append(index)

				last_word = word
				last_tag = tag
				s_index += 1
			index += 1

		# Make all the inferred items unique
		self.raw_operators = list(set(self.raw_operators))
		self.contexts = list(set(self.contexts))
		self.units = list(set(self.units))

		if len(self.contexts) > 1:
			op_key = OPERATOR_STR["multiple_contexts"]
		elif len(self.contexts) > 0:
			op_key = OPERATOR_STR["single_context"]
		else:
			op_key = OPERATOR_STR["no_context"]

		# Resolve the verbs to actual operators using the brain
		for o in self.raw_operators:
			op = p.brain.operator(o)
			if op != "eq" or len(self.raw_operators) == 1:
				self.operators.append(op_key[op])
		self.operators = list(set(self.operators))

		# Resolve the subordinates
		for o in self.conjunctions:
			conjunction, subordinate = o
			self.subordinates.append(p.brain.subordinate(subordinate))
		self.subordinates = list(set(self.subordinates))

		# Resolve the query
		self._possible_query(len(p.sentence_tags) - 1)
		for query_type in self.query_points:
			for i in self.query_points[query_type]:
				self._possible_query(i)
		high_score = 0
		for query_index in self.possible_queries:
			score = self.possible_queries[query_index]
			if score > high_score:
				high_score = score
				self.query = query_index
			elif score == high_score:
				self.query = None

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

		if self.query is not None:
			i.append("and asks a single question")
		else:
			i.append("however, I don't know what it wants for an answer")

		o.append("## Problem inference")
		if thought_any:
			o.append(" ".join(i) + ".")
		else:
			o.append("I have literally no idea what's going on here.")

		return "\n".join(o)
