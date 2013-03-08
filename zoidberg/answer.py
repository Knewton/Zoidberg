#!/usr/bin/env python

ANSWER_SYNTAX = {
	"expression": "is the solution to an expression.",
	"unit": "is the unit of the solution to an expression.",
	"context": "is the owner of the solution to an expression."
}

SOLUTION_WORKFLOW = {
	"plug_and_chug": "Extract symbols, construct expression, solve.",
	"contrast": "Create comparison expression to contrast solution values."
}

class Answer(object):
	def __init__(self, query):
		self.query = query

		self.syntax = None
		self.context = None
		self.unit = None
		self.subordinate = None
		self.workflow = None
		self.comparison = None

		self.execute()

	def execute(self):
		p = self.query.problem

		for v_part in self.query:
			val, part = v_part

			if part == "asking":
				self.syntax = p.brain.answer_syntax(val, str(self.query))

		# Everything below here is dragons whatfor should be slain
		print self.syntax
		return

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

		o.append("\n### {0}".format(self.query))

		if self.syntax:
			o.append("The answer {0}".format(ANSWER_SYNTAX[self.syntax]))

		return "\n".join(o)
