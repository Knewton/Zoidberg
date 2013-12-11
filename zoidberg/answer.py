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

# A Zoidberg answer refers to the structure and syntax of what the correct
# response to the problem should be. As a result, the "answer" to a question
# is an assertion as to what the correct answer will be; the "solution" to
# question is the actual correct response.
#
# Example:
#     Answer:   The unknown value of apples owned by everyone.
#     Solution: 6 apples
class Answer(object):
	def __init__(self, query):
		self.query = query

		self.syntax = None
		self.relative = False
		self.rel_mode = None
		self.comparator = None
		self.subordinates = []

		self.relative_value = False
		self.value = None
		self.unit = None
		self.context = None

		self.last_unrefined_context = None

		self.actor = None
		self.action = None

		self.execute()

	def execute(self):
		p = self.query.problem
		i = p.inference

		# The asking process determines what type of answer we want
		asking = False

		# The refining process determines the origin of our answer
		refining = False

		# The specifying process adds restrictions to an asnwer
		specifying = False

		for v_part in self.query:
			val, part, subtype = v_part
			#print val, part

			if part == "asking":
				self.syntax = p.brain.answer_syntax(val, str(self.query))
				asking = True

			if part == "rel_less":
				if asking:
					self.relative = True
					self.rel_mode = "su"

			if part == "rel_more":
				if asking:
					self.relative = True
					self.rel_mode = "ad"

			if part == "pre_ind_plu":
				if asking and self.last_unrefined_context:
					self.actor = self.last_unrefined_context
					self.last_unrefined_context = None

			# Specifying the acting is tantamount to ending the question
			if part == "acting":
				if asking:
					self.action = val
					asking = False
					refining = True
					specifying = True

			# assume unit appearing during asking for answer
			if part == "unit" and asking:
				self.unit = val

			if part == "comparator_context":
				self.comparator = val[0]

			# The qstart ends asking and begins refining
			if part == "q_start":
				asking = False
				refining = True

			# The qstop ends asking and begins specifying
			if part == "q_stop":
				refining = True
				specifying = True

			# assume context during refining is owner
			if part == "context":
				if refining:
					self.context = val
				else:
					self.last_unrefined_context = val

			# Assume subordinate during specifying is answer condition
			if part == "subordinate" and specifying:
				subs = self.query.subordinates
				self.subordinate = [s for s in subs if s[0] == val[0]]
				if len(self.subordinate) > 0:
					self.subordinates += self.subordinate

	def __str__(self):
		o = []

		o.append("\n### Question text")
		o.append(str(self.query))

		o.append("\n### Answer interpretation")

		is_req = False
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
		elif self.relative:
			if self.rel_mode == "su":
				mode = "difference in"
			elif self.rel_mode == "ad":
				mode = "increase in"
		else:
			mode = "unknown"
		i.append("the {0} {1} of".format(mode, syntax))

		if self.actor:
			i.append("{0} {1}".format(self.actor, self.action))

		if self.value:
			if self.relative_value:
				i.append("the")
			i.append(self.value)

		if self.unit:
			i.append(self.unit)

		if self.context:
			if self.query.problem.inference.is_requirement_problem:
				i.append("needed by {0}".format(self.context))
			else:
				i.append("owned by {0}".format(self.context))

		if self.relative:
			if self.comparator is not None:
				i.append("with respect to {0}".format(self.comparator))

		if len(self.subordinates) > 0:
			for sub in self.subordinates:
				w, s = sub
				if s is None or s == "place_noun":
					i.append(self.query.problem.inference.subordinate_strings[w])
				else:
					i.append(ANSWER_SUBORDINATE[s])

		o.append(" ".join(i) + ".")

		return "\n".join(o)

