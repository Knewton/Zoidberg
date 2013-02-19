#!/usr/bin/env python

class Query(object):
	def __init__(self, problem):
		self.problem = problem
		self._execute()

		self.answer_type = None
		self.context = None
		self.unit = None
		self.subordinate = None

	def _execute(self):
		p = self.problem
		i = p.inference

		if i.query is None:
			return

	def __str__(self):
		o = []

		o.append("## Query extraction")

		if self.answer_type is None:
			o.append("I have no idea what the answer type is.")

		return "\n".join(o)

