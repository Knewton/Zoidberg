#!/usr/bin/env python

ANSWER_FORMATS = {
	"expression": "Answer is an expression from the statement. (3, x, 4 cars)",
	"unit": "Answer is a unit (apples, cars)",
	"context": "Answer is a context (Mary, Dr. Jones)"
}

SOLUTION_WORKFLOW = {
	"plug_and_chug": "Extract symbols, construct expression, solve.",
	"contrast": "Create comparison expression to contrast solution values."
}

class Query(object):
	def __init__(self, problem):
		self.problem = problem

		self.query_sentence = None
		self.query_tags = None

		self.answer_format = None

		self.answer_unit = None
		self.context = None
		self.unit = None
		self.subordinate = None

		self.solution_workflow = None
		self.comparison_type = None

		self.execute()

	def execute(self):
		p = self.problem
		i = p.inference

		if len(i.queries) == 0:
			return

		return # @TODO: Remove this DEBUG break

		self.query_sentence = p.sentences[i.query]
		self.query_tags = p.sentence_tags[i.query]

		# Zoidberg is starting with what I think is like first grade word
		# problems. Understandably, the response to a question and extracting
		# it from text will require figuring out what the type of answer is
		# first, and then attempting to satisfy it. The "type" of answer could
		# be more complex than just solving some equation, and may as a more
		# intricate followup like "Who has more apples?" requiring a response
		# of "John" or "Mary" rather than 4 apples.
		#
		# However, again, Zoidber is starting with word problems for first
		# graders, the answer to which is always going to be some number.
		# Zoidberg is going to return units, because unlike a first grader,
		# he understands their importance as an intrinsic requirement of
		# being able to solve using them.
		#
		# This should also make it subtley faster to process the query. I mean
		# it's first grade math, this isn't exactly complicated thought.
		#
		# tl;dr Every question is a number until I learns me better schoolin'.
		self.answer_format = ANSWER_FORMATS["expression"]

		last_noun_tag = None

		for s_tag in self.query_tags:
			word, tag = s_tag

					# @NOTE: If I wasn't ignoring the fact questions could be
					# about other things, the two step process of determining
					# phrasing is likely a lovely place to figure out what the
					# answer type is, as well.

			if tag == "NNS": # Probably a unit
				if phrasing_question:
					if word in i.units:
						self.unit = word
						self.solution_workflow = "plug_and_chug"

			# JJR: Commparative adjective (bigger)
			# JJS: Superlative adjective (biggest)
			if tag in ["JJR", "JJS"]:
				self.solution_workflow = "plug_and_chug"
				self.comparison_type = p.brain.comparison(word)


	def __str__(self):
		o = []

		o.append("## Query extraction")
		if self.query_sentence is None:
			o.append("I couldn't even guess what the quesiton was.")
		else:
			o.append(self.query_sentence)

		return "\n".join(o)

