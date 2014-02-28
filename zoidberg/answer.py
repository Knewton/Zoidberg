#!/usr/bin/env python

OPERATOR_STR = {
	"eq": "owned by",
	"ad": "gained by",
	"mu": "gained by",
	"ex": "given to",
	"su": "lost by",
	"di": "lost by",
	"re": "required by",
	"co": "converted by",
	"cr": "created by",
	"cn": "used by",
}

ANSWER_SYNTAX = {
	"unknown": "unknown to me",
	"expression": "value",
	"unit": "unit",
	"context": "owner",
	"expression_connotation": "value",
	"eval_enum": "evaluation"
}

ANSWER_SUBORDINATE = {
	"time_starting": "at the beginning of the problem",
	"time_ending": "at the end of the problem",
	"context_grouping": "added together",
	"unit_grouping": "totaled up",
	"unit_requirement": "needed to equal the specified value",
	"comparator": "quantities",
	"costpay": "costing"
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

		self.solved_contexts = []

		self.constant = None
		self.syntax = None
		self.relative = False
		self.rel_mode = None
		self.comparator = None
		self.comparator_unit = None
		self.subordinates = []
		self.operator = None

		self.relative_value = False
		self.value = None
		self.unit = None
		self.context = None
		self.context_constant = None
		self.context_subtype = None

		self.last_unrefined_context = None
		self.last_unrefined_context_subtype = None

		self.actor = None
		self.actor_subtype = None
		self.action = None

		self.last_adj = None
		self.unit_adjectives = {}

		self.connotation_tag = None

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
			#rint val, part

			if part == "asking":
				self.syntax = p.brain.answer_syntax(val, str(self.query))
				asking = True
				if self.syntax == "expression_connotation":
					tag = p.brain.connotation(val, str(self.query))
					self.connotation_tag = tag
					if self.connotation_tag == "money":
						self.unit = "money"
					else:
						self.unit = p.brain.connotation_unit(tag, p.units)

			if part == "rel_less":
				if asking:
					self.relative = True
					self.rel_mode = "su"
				elif refining:
					self.rel_mode = "su"

			if part == "rel_more":
				if asking:
					self.relative = True
					self.rel_mode = "ad"
				elif refining:
					self.rel_mode = "ad"

			if part == "pre_ind_plu":
				if asking and self.last_unrefined_context:
					self.actor = self.last_unrefined_context
					self.actor_subtype = self.last_unrefined_context_subtype
					self.last_unrefined_context = None
					self.last_unrefined_context_subtype = None

			# Specifying the acting is tantamount to ending the question
			if part in ["acting", "acting_inferred"]:
				if asking:
					self.action = val
					asking = False
					refining = True
					specifying = True
					if self.last_unrefined_context:
						self.actor = self.last_unrefined_context
						self.actor_subtype = self.last_unrefined_context_subtype
						self.last_unrefined_context = None
						self.last_unrefined_context_subtype = None
			if part == "money":
				val = "money"
				part = "unit"

			# assume unit appearing during asking for answer
			if part in ["unit", "unit_inferred"] and asking:
				if self.last_adj is not None:
					if not val in self.unit_adjectives:
						self.unit_adjectives[val] = []
					self.unit_adjectives[val].append(self.last_adj)
				self.unit = val

			if part in ["unit", "unit_inferred"] and refining and self.unit == None:
				self.unit = val

			if part in ["comparator_context", "comparator_context_inferred"]:
				if isinstance(val, basestring):
					self.comparator = val
				else:
					self.comparator = val[0]

			if part == "constant":
				self.constant = val

			# The qstart ends asking and begins refining
			if part == "q_start":
				asking = False
				refining = True

			# The qstop ends asking and begins specifying
			if part == "q_stop":
				self.operator = p.brain.operator(val, str(self.query))
				refining = True
				specifying = True

			# assume context during refining is owner
			if part in ["context", "context_inferred"]:
				if refining:
					self.context = val
					self.context_subtype = subtype
				else:
					self.last_unrefined_context = val
					self.last_unrefined_context_subtype = subtype
				if self.constant:
					self.context_constant = self.constant
					self.constant = None

			# Assume subordinate during specifying is answer condition
			if part in ["subordinate", "subordinate_inferred"]:
				stype = self.query.subordinate_lookup[val[0]]
				if stype == "refiner":
					if self.action:
						self.action = " ".join([self.action, val[0]])
				elif stype == "context_grouping":
					if len(self.query.problem.subordinate_adaptive_contexts) > 0:
						sac = self.query.problem.subordinate_adaptive_contexts[0]
						self.context = sac
						self.context_subtype = subtype
				elif not specifying and self.actor is not None and self.query.problem.exestential:
				# If we have an actor but are not specifying in an exestential
				# problem, then we can simply assume that specification is occurring
					specifying = True

				if stype in ["place_noun", "time_ending", "time_starting"]:
					specifying = True

				#rint specifying
				if specifying:
					subs = self.query.subordinates
					self.subordinate = [s for s in subs if s[0] == val[0]]
					#rint subs, stype, val[0]
					if len(self.subordinate) > 0:
						self.subordinates += self.subordinate

				if stype == "comparator":
					self.comparator_unit = val[0]

				#rint "Here", stype, val, self.subordinates

			if part == "adjective":
				self.last_adj = val
			else:
				self.last_adj = None

	def __str__(self):

		if self.context_subtype and self.context_subtype[0] == "self":
			self.context = self.query.problem.brain.self_reflexive(self.context, True)

		o = []

		o.append("\n### Question text")
		o.append("    " + str(self.query))

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
				surprised = self.context is not None
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
		if self.syntax is not None:
			if self.syntax == "eval_enum":
				i.append("the {0} of".format(syntax))
			else:
				i.append("the {0} {1} of".format(mode, syntax))

		if self.actor:
			if self.action is not None:
				i.append("{0} {1}".format(self.actor, self.action))
			else:
				i.append(self.actor)

		if self.value:
			if self.relative_value:
				i.append("the")
			i.append(self.value)

		if self.unit and not self.actor:
			if not self.relative and self.syntax == "context":
				if self.rel_mode == "su":
					i.append("less")
				elif self.rel_mode == "ad":
					i.append("more")
			i.append(self.unit)

		if self.context:
			cntx = self.context
			if self.context_constant:
				cntx = " ".join([self.context_constant, cntx])
			if self.query.problem.inference.is_requirement_problem:
				i.append("needed by {0}".format(cntx))
			elif self.operator is not None:
				i.append("{1} {0}".format(cntx, OPERATOR_STR[self.operator]))
			else:
				# Assume equals failing all else?
				i.append("{1} {0}".format(cntx, OPERATOR_STR["eq"]))

		if self.relative:
			if self.comparator is not None:
				i.append("with respect to {0}".format(self.comparator))
			elif self.comparator_unit is not None:
				i.append("with respect to {0}".format(self.comparator_unit))

		if len(self.subordinates) > 0:
			did_subs = []
			for sub in self.subordinates:
				w, s = sub
				if s in did_subs:
					continue

				did_subs.append(s)
				if s is None or s == "place_noun":
					i.append(self.query.problem.inference.subordinate_strings[w])
				else:
					i.append(ANSWER_SUBORDINATE[s])

		o.append("    " + " ".join(i) + ".")

		return "\n".join(o)

