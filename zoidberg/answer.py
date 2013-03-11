#!/usr/bin/env python

ANSWER_SYNTAX = {
	"unknown": "unknown to me",
	"expression": "value",
	"unit": "unit",
	"context": "owner"
}

ANSWER_SUBORDINATE = {
	"time_starting": "at the beginning of the problem",
	"time_ending": "at the end of the problem"
}

class Answer(object):
	def __init__(self, query):
		self.query = query

		self.syntax = None
		self.subordinate = None

		self.relative_value = False
		self.value = None
		self.unit = None
		self.context = None

		self.execute()

	def execute(self):
		p = self.query.problem

		# The asking process determines what type of answer we want
		asking = False

		# The refining process determines the origin of our answer
		refining = False

		# The specifying process adds restrictions to an asnwer
		specifying = False

		for v_part in self.query:
			val, part, subtype = v_part

			if part == "asking":
				self.syntax = p.brain.answer_syntax(val, str(self.query))
				asking = True

			# assume unit appearing during asking for answer
			if part == "unit" and asking:
				self.unit = val

			# The qstart ends asking and begins refining
			if part == "q_start":
				asking = False
				refining = True

			# The qstart ends asking and begins specifying
			if part == "q_stop":
				refining = True
				specifying = True

			# assume context during refining is owner
			if part == "context" and refining:
				self.context = val

			# Assume subordinate during specifying is answer condition
			if part == "subordinate" and specifying:
				subs = self.query.subordinates
				self.subordinate = [s for s in subs if s[0] == val[0]]
				if len(self.subordinate) > 0:
					self.subordinate = self.subordinate[0][1]
				else:
					self.subordinate = None

	def __str__(self):
		o = []

		o.append("\n### Question")
		o.append(str(self.query))

		o.append("\n#### Answer interpretation")

		i = ["The answer is"]

		# Are we surprised about the answer format?
		surprised = False
		if self.syntax is None:
			i.append(ANSWER_SYNTAX["unknown"])
		else:
			if self.syntax == "expression" and not self.relative_value:
				surprised = self.value is not None
			elif self.syntax == "unit":
				surprised = self.unit is not None
			elif self.syntax == "context":
				surprised = self.unit is not None
			syntax = ANSWER_SYNTAX[self.syntax]

		if surprised:
			mode = "surprisingly known"
		else:
			mode = "unknown"
		i.append("the {0} {1} of".format(mode, syntax))

		if self.value:
			if self.relative_value:
				i.append("the")
			i.append(self.value)

		if self.unit:
			i.append(self.unit)

		if self.context:
			i.append("owned by {0}".format(self.context))

		if self.subordinate:
			i.append(ANSWER_SUBORDINATE[self.subordinate])

		o.append(" ".join(i) + ".")

		return "\n".join(o)

