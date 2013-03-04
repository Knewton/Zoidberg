#!/usr/bin/env python

ANSWER_FORMATS = {
	"expression": "Answer is an expression from the statement. (3, x, 4 cars)",
	"unit": "Answer is a unit (apples, cars)",
	"context": "Answer is a context (Mary, Dr. Jones)"
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

		self._execute()

	def _execute(self):
		p = self.problem
		i = p.inference

		if i.query is None:
			return

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

		# Is the question being phrased?
		# This is used as a tristate over a boolean, with None as "maybe" state
		phrasing_question = False

		for s_tag in self.query_tags:
			word, tag = s_tag
			if tag in ["WRB", "WDT", "WP", "WP$"]: # Wh- determiner
				phrasing_question = None # Maybe phrasing

			if tag == "JJ": # Adjective
				if phrasing_question is None:
					phrasing_question = True
					# @NOTE: If I wasn't ignoring the fact questions could be
					# about other things, the two step process of determining
					# phrasing is likely a lovely place to figure out what the
					# answer type is, as well.

	def __str__(self):
		o = []

		o.append("## Query extraction")
		if self.query_sentence is None:
			o.append("I couldn't even guess what the quesiton was.")
		else:
			o.append(self.query_sentence)

		return "\n".join(o)

