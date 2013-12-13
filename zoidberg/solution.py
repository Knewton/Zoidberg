#!/usr/bin/env python

from sympy import Symbol, Function, Derivative
from sympy.core.power import Pow
from sympy import Eq, Rational
from sympy.solvers import solve

OPERATOR_STR = {
	"eq": "owned by",
	"ad": "gained by",
	"mu": "gained by",
	"su": "lost by",
	"di": "lost by",
	"ans": "finally owned by"
}

OP_DISPLAY = {
	"ans": "==",
	"eq": "=",
	"eqx": "=",
	"ad": "+",
	"mu": "*",
	"su": "-",
	"di": "/",
	"re": "==",
	"co": "->"
}

def number(s):
	try:
		return float(s) if '.' in s else int(s)
	except ValueError:
		return -1

class Solution(object):
	def __init__(self, problem):
		self.problem = problem
		self.last_index = 0

		self.zeroes_out = False

		self.last_container = None
		self.last_action = None
		self.last_actor = None

		self.context = None
		self.context_subtype = None
		self.operator = None
		self.constant = None
		self.unit = None
		self.comparator_context = None
		self.relative = False
		self.rel_mode = None

		self.sentence_data = []
		self.data = None
		self.actor_data = None
		letters = [chr(x) for x in xrange(ord("a"), ord("z")+1)]
		self.varpool = letters[-3:] + letters[:-3]

		self.beginning_vars = []
		self.middle_vars = []
		self.ending_vars = []

		self.varsfor = {}
		self.used_vars = []
		self.symbols = {}
		self.work = {}
		self.correct_responses = []

		self.container = None
		self.containers = None
		self.actor = None
		self.action = None

		self.execute()

	def store_var(self, idx, var, eq):
		if idx == 0:
			self.beginning_vars.append((var, eq))
		elif idx == self.last_index:
			self.ending_vars.append((var, eq))
		else:
			self.middle_vars.append((var, eq))

	def get_symbol(self, context, unit, container, idx=-1, operator=None, constant=None, readonly=True):
		if context is None or unit is None:
			return (False, Symbol("BROKEN"), "BROKEN", "BROKEN")

		s = [context, unit]
		dcontainer = None
		if container is not None and container != "_unknown_":
			s.append(container)
			if container in self.problem.inference.subordinate_strings:
				dcontainer = self.problem.inference.subordinate_strings[container]

		sym = " ".join(s)
		first_time = sym not in self.symbols
		hindsight_inference = False
		if first_time:
			self.symbols[sym] = Symbol(sym)

		symbol = self.symbols[sym]
		if first_time and operator != "eq" and constant is None:
			# Make an assumption that if the first thing we're
			# doing is an addition, that we started with 0 units
			symbol = 0
			hindsight_inference = True

		just_defined = False
		if constant is None and not readonly:
			var = self.newvar()
			self.varsfor[var] = (sym, operator)

			k = "{0} {1} {2}".format(unit, OPERATOR_STR[operator], context)

			if not k in self.work:
				self.work[k] = []
			self.work[k].append("= " + var)

			constant = self.symbols[var]
			just_defined = True
			if hindsight_inference:
				self.store_var(idx, var, constant)
		else:
			var = str(constant)

		#print idx, sym, operator

		if sym[0:1] == "@":
			dsym = "{0} {1}".format(context[1:], unit)
		else:
			dsym = sym

		if dcontainer is not None:
			dsym += " " + dcontainer

		if not dsym in self.work:
			self.work[dsym] = []

		if operator is not None and constant is not None:
			if operator in ["eq", "eqx", "re"]:
				self.store_var(idx, sym, constant)
				symbol = constant
				if operator != "eqx":
					self.work[dsym].append("= " + str(constant))
			elif operator == "ad":
				symbol += constant
				if hindsight_inference:
					self.work[dsym].append("= " + str(constant))
				else:
					self.work[dsym].append("+ " + str(constant))
			elif operator == "su":
				symbol -= constant
				if hindsight_inference:
					self.work[dsym].append("= " + str(constant))
				else:
					self.work[dsym].append("- " + str(constant))
			elif operator == "mu":
				symbol *= constant
				if hindsight_inference:
					self.work[dsym].append("= " + str(constant))
				else:
					self.work[dsym].append("* " + str(constant))
			elif operator == "di":
				symbol /= constant
				if hindsight_inference:
					self.work[dsym].append("= " + str(constant))
				else:
					self.work[dsym].append("/ " + str(constant))
			else:
				return (hindsight_inference, symbol, var, sym)
			self.symbols[sym] = symbol

		return (hindsight_inference, symbol, var, sym)

	def reset_extractor(self):
		if self.action is not None:
			self.last_action = self.action

		if self.actor is not None:
			self.last_actor = self.actor

		if self.container is not None:
			self.last_container = self.container

		self.container = None
		self.actor = None
		self.action = None
		self.context = None
		self.context_subtype = None
		self.operator = None
		self.constant = None
		self.unit = None
		self.comparator_context = None
		self.relative = False
		self.rel_mode = None

	def generate_expression(self, zeroes_out=False):
		if self.data is None:
			self.data = {}
		if self.actor_data is None:
			self.actor_data = {}

		actor = "@{0}".format(self.actor)
		action = self.action
		context = self.context
		operator = self.operator
		constant = self.constant
		container = self.container
		unit = self.unit
		data = None
		sym = None

		if context is None:
			context = "_unknown_"

		if unit is None:
			unit = "_unknown_"

		sym = " ".join([context, unit])

		k1, k2 = None, None
		if actor and action:
			if actor not in self.actor_data:
				self.actor_data[actor] = {}

			if action not in self.actor_data[actor]:
				self.actor_data[actor][action] = []

			# Assume an equality in this case
			if operator is None and constant is not None:
				operator = "eq"

			data = self.actor_data[actor][action]
			k1 = actor
			k2 = action
		else:
			if self.last_action is not None and context == self.last_actor:
				actor = "@{0}".format(self.last_actor)
				action = self.last_action

				if not actor in self.actor_data:
					self.actor_data[actor] = {}

				if not action in self.actor_data[actor]:
					self.actor_data[actor][action] = []

				if container is None and self.last_container is not None:
					container = self.last_container

				# Only one action for the actor, so it's likely this
				data = self.actor_data[actor][action]

				k1 = actor
				k2 = action
			else:
				if context not in self.data:
					self.data[context] = {}

				if unit not in self.data[context]:
					self.data[context][unit] = []

				data = self.data[context][unit]
				k1 = context
				k2 = unit
				sym = " ".join([context, unit])

		if data is not None:
			if self.relative and self.comparator_context:
				osym = sym
				sym = " ".join([self.comparator_context, unit])
				if operator == "eq":
					operator = self.rel_mode
					data.append(("eqx", sym))
					if not osym in self.work:
						self.work[osym] = []
					self.work[osym].append("= " + str(sym))

			data.append((operator, constant))
			if zeroes_out:
				data.append(("ans", "0"))

		# If nothing was done there's nothing to do
		if len(data) == 0:
			self.data = None
			self.actor_data = None
			self.containers = None

		if container is None:
			container = "_unknown_"

		if container is not None:
			if self.containers is None:
				self.containers = {}

			if not container in self.containers:
				self.containers[container] = {}

			if not k1 in self.containers[container]:
				self.containers[container][k1] = {}

			self.containers[container][k1][k2] = data

		self.reset_extractor()

	def has_any(self):
		return self.container or self.context or self.operator or self.constant or self.unit

	def has_all(self):
		a = self.container and self.context and self.operator and self.constant and self.unit
		if self.relative:
			if not self.comparator_context:
				return False

		return a

	def execute(self):
		p = self.problem
		i = p.inference

		self.last_index = len(i.sentences) - 1

		for parser in i.sentences:
			# Sometimes one context will transfer to another. In those cases
			# we only want to change the context to the primary one
			did_set_context = False
			last_context = None
			last_context_subtype = None
			last_container = None
			zeroes_out = False
			for v_part in parser.parsed:
				val, part, subtype = v_part

				if part == "context":
					if not did_set_context:
						did_set_context = True
						self.context = val
						self.context_subtype = subtype
					last_context = val
					last_context_subtype = subtype

				if part == "operator" and not self.operator:
					self.operator = parser.operator[val]
					if self.operator == "co":
						self.operator = None

				if part == "constant" and not self.constant:
					self.constant = val

				if part == "unit":
					self.unit = val

				if part == "solution_zero":
					zeroes_out = True
					self.zeroes_out = True

				if part in "rel_less":
					self.rel_mode = "su"
					self.relative = True

				if part in "rel_more":
					self.rel_mode = "ad"
					self.relative = True

				if part == "comparator_context":
					self.comparator_context = val[0]

				if part == "pre_ind_plu":
					if last_context and not self.actor:
						self.actor = last_context
						last_context = None
						last_context_subtype = None

				if part == "acting":
					if self.actor:
						self.action = val

				if part == "subordinate":
					if val[1] is not None:
						# If we have a conjunction we have an container
						self.container = val[0]
						last_container = self.container

				if part == "coordinating_conjunction":
					#print "Restore context and container"
					self.context = last_context
					self.context_subtype = last_context_subtype
					self.container = last_container

				if self.has_all():
					#print "Here and", zeroes_out
					self.generate_expression(zeroes_out)

				# @TODO: DEBUG
				#print val
				#print part
				#print subtype
				#print "----"

			if self.has_any():
				self.generate_expression(zeroes_out)
			else:
				self.reset_extractor()

			if self.containers is not None:
				self.sentence_data.append(self.containers)
				self.data = None
				self.actor_data = None
				self.containers = None

	def newvar(self):
		sym = self.varpool.pop(0)
		self.used_vars.append(sym)
		self.symbols[sym] = Symbol(sym)
		return sym

	def compute(self):
		index = 0
		p = self.problem
		last_context = None
		switch_context = False
		new_sentence_data = []
		for sd in self.sentence_data:
			new_container = {}
			for container in sd:
				data = sd[container]
				new_data = {}
				for context in data:
					units = data[context]

					# use the last context for inclusive context
					if p.brain.is_inclusive(context):
						if last_context is not None:
							context = last_context
							switch_context = True
						else:
							# @todo: this state should probably never happen?
							# a context that is inclusive should have one context
							# that preceeds it
							print "Well this is a fine mess"
							exit(1)
					else:
						switch_context = False

					new_units = {}
					for unit in units:
						# We increment at the start because of the bail-out nature
						data_index = -1

						new_values = []
						for values in units[unit]:
							data_index += 1
							operator, constant = values

							if constant in self.symbols:
								constant = self.symbols[constant]
							elif constant is not None:
								# Convert and type the constant properly
								constant = number(constant)

							# Apply the operation to the symbol
							if operator is not None:
								inf, symbol, con, sym = self.get_symbol(context,
										unit, container, index, operator, constant, False)
							#	if inf:
							#		new_values.append(("eq", "0"))
							else:
								con = constant
							new_values.append((operator, con))
						new_units[unit] = new_values
					new_data[context] = new_units
					last_context = context
				new_container[container] = new_data
			index += 1
			new_sentence_data.append(new_container)
		self.sentence_data = new_sentence_data
#		print self.sentence_data

	def compute_correct(self):
		self.compute()

		p = self.problem
		i = p.inference
		q = p.question

		def add_response(val, unit, idx):
			for v in val:
				i = [str(v)]
				if unit is not None:
					i.append(unit)
				self.correct_responses.insert(idx, " ".join(i))

		def safe_solve(*args):
			try:
				return solve(*args)
			except Exception as e:
				print str(e)
				return "??"

		def simple_solve(sym):
			for c in [Symbol, Function, Pow, Derivative]:
				if isinstance(sym, c):
					return safe_solve(sym, sym)
			return [sym]

		index = 0
		for answer in q.answers:
			needEqu = True
			dispSym = None
			if answer.actor and answer.action:
				needEqu = False
				# The answer in actor/action questions is the actor normally?
				answer.unit = answer.actor
				inf, equ, con, sym = self.get_symbol("@" + answer.actor, answer.action, None, index)

			resp = None
			dontSave = False
			compContext = None

			if len(answer.subordinates) > 0:
				working_answer = None
				for s in answer.subordinates:
					word, sub = s
					if sub == "time_ending":
						l = len(self.ending_vars)

						if needEqu:
							inf, equ, con, sym = self.get_symbol(answer.context, answer.unit, None, index)

						if l == 1:
							symbol = self.symbols[self.ending_vars[0]]
							resp = (safe_solve(equ, symbol), answer.unit)
						elif l == 0:
							resp = (simple_solve(equ), answer.unit)
						else:
							self.correct_responses.append(
								"Not sure; too many ending variables!")
					elif sub == "time_starting":
						l = len(self.beginning_vars)
						if needEqu:
							inf, equ, con, sym = self.get_symbol(answer.context, answer.unit, None, index)
						if l == 1:
							name, symbol = self.beginning_vars[0]
							resp = (safe_solve(equ, symbol), answer.unit)
						elif l == 0:
							resp = (simple_solve(equ), answer.unit)
						else:
							self.correct_responses.append(
								"Not sure; too many starting variables!")
					elif sub == "context_grouping":
						ans = 0
						syms = []
						for c in self.problem.adaptive_context[answer.context]:
							context, context_subtype = c
							sinf, sequ, scon, ssym = self.get_symbol(context, answer.unit, None)
							self.work[ssym].append("= " + " + ".join(syms))
							syms.append(ssym)
							ans += sequ
						resp = (simple_solve(ans), answer.unit)
					elif sub == "place_noun" or sub is None:
						compContext = word
						if answer.actor and answer.action:
							inf, equ, con, sym = self.get_symbol("@" + answer.actor, answer.action, word, index)
						else:
							inf, equ, con, sym = self.get_symbol(answer.context, answer.unit, word, index)
						resp = (simple_solve(equ), answer.unit)
					else:
						dontSave = True
						self.correct_responses.append("No sure; unknown subordinate type {0} ({1})".format(sub, word))
			else:
				if needEqu:
					inf, equ, con, sym = self.get_symbol(answer.context, answer.unit, None, index)
				resp = (simple_solve(equ), answer.unit)

			if answer.relative:
				inf, equ, con, sym = self.get_symbol(answer.context, answer.unit, None, index)
				if answer.comparator is not None:
					coinf, comp, conc, csym = self.get_symbol(answer.comparator, answer.unit, compContext)
				else:
					coinf, comp, conc, csym = self.get_symbol(answer.context, answer.unit, None)

				r = None

				if resp is None:
					r = equ
				else:
					r, u = resp
					# We will have already solved the equation by this point
					r = r[0]

				k = "Answer"
				if not k in self.work:
					self.work[k] = []

				# ad(dition): how many more
				if answer.rel_mode == "ad":
					v = r - comp
					unt = ["more"]
					self.work[k].append("= " + sym +" - " + csym)
					self.work[k].append("= " + str(equ) +" - " + str(comp))
				# su(btraction) how many fewer
				elif answer.rel_mode == "su":
					v = comp - r
					unt = ["fewer"]
					self.work[k].append("= " + csym +" - " + sym)
					self.work[k].append("= " + str(comp) +" - " + str(equ))

				if answer.unit:
					unt.append(answer.unit)

				resp = (simple_solve(v), " ".join(unt))

			if not dontSave:
				r, u = resp
				#print r, u, resp
				if self.zeroes_out:
					self.work[sym].append("= 0")
				add_response(r, u, index)

			index += 1

	def __str__(self):
		o = []

		o.append("\n## Data extraction")
		index = 1
		for sd in self.sentence_data:
			for container in sd:
				data = sd[container]
				s = []
				for context in data:
					for unit in data[context]:
						for values in data[context][unit]:
							operator, constant = values
							i = []

							actor = None
							action = None

							if context is not None and context[0:1] == "@":
								actor = context[1:]
								action = unit
								unit = None
								context = None

							if context == "_unknown_":
								context = None

							if unit == "_unknown_":
								unit = None

							if container is None or container == "_unknown_":
								container = None
							elif container in  self.problem.inference.subordinate_strings:
								container = self.problem.inference.subordinate_strings[container]

							display_constant = constant
							if display_constant is None:
								display_constant = "<an unknown number>"

							if operator is None or operator == "co":
								continue # Probably the question

							if actor is not None and action is not None:
								i.append(action)
								i.append(actor)

								if container is not None:
									i.append(container)

								i.append(OP_DISPLAY[operator])
								i.append(display_constant)
							elif context is not None and unit is not None:

								i.append(unit)
								if operator is not None and operator == "re":
									i.append("needed by")
								else:
								#	i.append(OPERATOR_STR[operator])
									i.append("owned by")

#								if self.problem.inference.is_requirement_problem:

								i.append(context)

								if container is not None:
									i.append(container)

								i.append(OP_DISPLAY[operator])
								i.append(display_constant)
							else:
								did_something = False
								i.append("I don't know how to format this!")

							s.append(" ".join(i))

				if len(s) > 0:
					o.append("\n### Sentence {0}".format(index))
					o.append("\n".join(s))
			index += 1

#		if len(self.work) > 0:
#			o.append("\n## Show your work")
#			ans = None
#			if "Answer" in self.work:
#				ans = self.work["Answer"]
#				del self.work["Answer"]
#
#			for symbol, work in self.work.iteritems():
#				if len(work) > 0:
#					o.append("{0} {1}".format(symbol, " ".join(work)))
#			if ans is not None:
#				if len(ans) > 0:
#					o.append("{0} {1}".format("Answer", " ".join(ans)))

		if len(self.correct_responses) > 0:
			o.append("\n## Correct response")
			index = 1
			for response in self.correct_responses:
				if len(self.correct_responses) > 1:
					o.append("\n### Response {0}".format(index))
				o.append(response)
				index += 1

		return "\n".join(o)
