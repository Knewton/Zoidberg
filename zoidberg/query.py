#!/usr/bin/env python

from answer import Answer

class Query(object):
	def __init__(self, problem):
		self.problem = problem

		# The queries are the detected sentences which ask questions that need
		# to be answered in the word problem.
		self.queries = []

		# Answers to each query asked.
		self.answers = []

		self.execute()

	def execute(self):
		p = self.problem
		i = p.inference

		if len(i.queries) == 0:
			return

		for index in i.queries:
			sentence = i.sentences[index]
			self.queries.append(sentence)
			self.answers.append(Answer(sentence))

	def __str__(self):
		o = []

		o.append("## Answer formulation")
		for a in self.answers:
			o.append(str(a))

		return "\n".join(o)

