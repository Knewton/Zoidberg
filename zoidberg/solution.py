#!/usr/bin/env python

from sympy import Symbol, Function, Derivative, simplify
from sympy.core.power import Pow
from sympy import Eq, Rational
from sympy.solvers import solve
from json import dumps

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
	"co": "=>",
	"ex": "->"
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
		self.sig_figs = -1 # Don't need to use significant figures

		self.uses_context_constant = True
		self.answer_out = False
		self.asking = True
		self.symbol_answer = False
		self.descriptive_units = []
		self.did_combine_units = False
		self.coordinated_container = None
		self.coordinated = False
		self.zeroes_out = False
		self.relational_var = None

		self.last_container = None
		self.last_action = None
		self.last_actor = None

		self.context = None
		self.context_constant = None
		self.target = None
		self.can_target = False
		self.ex_op = False
		self.context_subtype = None
		self.target_subtype = None
		self.operator = None
		self.constant = None
		self.variable_relationship = None
		self.unit = None
		self.units = []
		self.context_unit = None
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

	def get_symbol(self, context, context_constant, unit, container, idx=-1, operator=None, constant=None, readonly=True, conref=None):
		if context is None and unit is not None:
			context = "_unknown_"
		if context is None or unit is None:
			#raise Exception
			return (False, Symbol("BROKEN"), "BROKEN", "BROKEN")

		s = [context, unit]
		dcontainer = None
		if container is not None and container != "_unknown_":
			s.append(container)
			if container in self.problem.inference.subordinate_strings:
				dcontainer = self.problem.inference.subordinate_strings[container]

		if context_constant is None:
			context_constant = "_unknown_"

		if not context_constant in self.symbols:
			self.symbols[context_constant] = {}

		sym = " ".join(s)
		first_time = sym not in self.symbols[context_constant]
		hindsight_inference = False

		if first_time:
			self.symbols[context_constant][sym] = Symbol(sym)

		symbol = self.symbols[context_constant][sym]
		if first_time and operator != "eq":
			# Make an assumption that if the first thing we're
			# doing is an addition, that we started with 0 units
			symbol = 0
			hindsight_inference = True

		#rint symbol, operator, readonly, constant, conref

		just_defined = False
		if constant is None and not readonly:
			var = self.newvar(context_constant)
			self.varsfor[var] = (sym, operator)

			k = "{0} {1} {2}".format(unit, OPERATOR_STR[operator], context)

			if not k in self.work:
				self.work[k] = []
			self.work[k].append("= " + var)

			constant = self.symbols[context_constant][var]
			just_defined = True
			if hindsight_inference:
				self.store_var(idx, var, constant)
		else:
			var = str(constant)

		#rint idx, sym, operator

		if sym[0:1] == "@":
			dsym = "{0} {1}".format(context[1:], unit)
		else:
			dsym = sym

		if dcontainer is not None:
			dsym += " " + dcontainer

		if not dsym in self.work:
			self.work[dsym] = []

#		rint "OTAY", sym, operator, constant
		if operator is not None and constant is not None:
			if operator in ["eq", "eqx", "re"]:
				self.store_var(idx, sym, constant)

				if self.relational_var is None:
#					rint "HERE"
					symbol = constant
				else:
					if conref:
						self.symbols[context_constant][conref] = constant.subs(Symbol(self.relational_var), symbol).evalf()
#					rint "THAR"
					# some cases we may already have a relational value so we
					# need to simply solve for the value already
					symbol = symbol.subs(Symbol(self.relational_var), constant).evalf()

				#rint "setting symbol"
				#raise Exception
				if operator != "eqx":
					self.work[dsym].append("= " + str(constant))
			elif operator == "ad":
				if self.relational_var is None:
					symbol += constant
				else:
					if conref:
						self.symbols[context_constant][conref] = constant.subs(Symbol(self.relational_var), symbol).evalf()

					# some cases we may already have a relational value so we
					# need to simply solve for the value already
					symbol = symbol + constant.subs(Symbol(self.relational_var), symbol).evalf()
				if hindsight_inference:
					self.work[dsym].append("= " + str(constant))
				else:
					self.work[dsym].append("+ " + str(constant))
			elif operator == "su":
				if self.relational_var is None:
					symbol -= constant
				else:
					if conref:
						self.symbols[context_constant][conref] = constant.subs(Symbol(self.relational_var), symbol).evalf()

					# some cases we may already have a relational value so we
					# need to simply solve for the value already
					symbol = symbol - constant.subs(Symbol(self.relational_var), symbol).evalf()

				if hindsight_inference:
					self.work[dsym].append("= " + str(constant))
				else:
					self.work[dsym].append("- " + str(constant))
			elif operator == "ans":
				self.symbol_answer = True
				sx = Eq(symbol, constant)
				if sx is False:
					symbol = Eq(Symbol(sym) + symbol, constant)
				else:
					symbol = sx
			elif operator == "ex":
				raise Exception
			elif operator == "mu":
				if self.relational_var is None:
					symbol *= constant
				else:
					if conref:
						self.symbols[context_constant][conref] = constant.subs(Symbol(self.relational_var), symbol).evalf()

					# some cases we may already have a relational value so we
					# need to simply solve for the value already
					symbol = symbol * constant.subs(Symbol(self.relational_var), symbol).evalf()
				if hindsight_inference:
					self.work[dsym].append("= " + str(constant))
				else:
					self.work[dsym].append("* " + str(constant))
			elif operator == "di":
				if self.relational_var is None:
					symbol /= constant
				else:
					if conref:
						self.symbols[context_constant][conref] = constant.subs(Symbol(self.relational_var), symbol).evalf()

					# some cases we may already have a relational value so we
					# need to simply solve for the value already
					symbol = symbol / constant.subs(Symbol(self.relational_var), symbol).evalf()
				if hindsight_inference:
					self.work[dsym].append("= " + str(constant))
				else:
					self.work[dsym].append("/ " + str(constant))
			else:
				return (hindsight_inference, symbol, var, sym)
			self.symbols[context_constant][sym] = symbol
			#rint self.symbols

		return (hindsight_inference, symbol, var, sym)

	def reset_extractor(self):
		if self.action is not None:
			self.last_action = self.action

		if self.actor is not None:
			self.last_actor = self.actor

		if self.container is not None:
			self.last_container = self.container

		self.asking = False
		self.container = None
		self.actor = None
		self.action = None
		self.context = None
		self.context_constant = None
		self.context_subtype = None
		self.target = None
		self.target_subtype = None
		if not self.ex_op:
			self.operator = None
		self.constant = None
		self.variable_relationship = None
		self.unit = None
		self.context_unit = None
		self.comparator_context = None
		self.relative = False
		self.rel_mode = None

	def generate_expression(self, zeroes_out=False, answer_out=False):
		if self.data is None:
			self.data = {}
		if self.actor_data is None:
			self.actor_data = {}

		actor = "@{0}".format(self.actor)
		action = self.action
		context = self.context
		context_constant = self.context_constant
		target = self.target
		target_constant = "_unknown_" # todo: assumed for now
		operator = self.operator
		constant = self.constant
		context_var = None
		container = self.container
		unit = self.unit
		context_unit = self.context_unit
		var_r = self.variable_relationship
		data = None
		sym = None

		if constant is None and operator is None and self.asking:
			self.reset_extractor()
			return None

		if constant is None and self.ex_op:
			operator = None

		if container is None:
			container = "_unknown_"

		if context is None:
			context = "_unknown_"

		if unit is None:
			unit = "_unknown_"

		if context_unit is None:
			sym = " ".join([context, unit])
		else:
			sym = " ".join([context, context_unit[1]])

		if context_constant == None:
			context_constant = "_unknown_"

		#rint context_unit

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
				if context_unit is not None:
					cu_context = context_unit[2]
					cu_unit = context_unit[1]

					if cu_context not in self.data:
						self.data[cu_context] = {}

					if cu_unit not in self.data[cu_context]:
						self.data[cu_context][cu_unit] = []

					if context not in self.data:
						self.data[context] = {}

					if cu_unit not in self.data[context]:
						self.data[context][cu_unit] = []

					data = self.data[cu_context][cu_unit]
					k1 = cu_context
					k2 = cu_unit
					sym = " ".join([cu_context, cu_unit])

					cu_data = self.data[context][cu_unit]
					cu_k1 = context
					cu_k2 = cu_unit

					#rint "Processing relative var"
					#raise Exception

					cinf, csymbol, ccon, cvar = self.get_symbol(cu_context,
							context_constant, cu_unit, container)
					inf, symbol, con, var = self.get_symbol(context,
							context_constant, cu_unit, container)

#					self.symbols[var] = self.symbols[cvar] * number(var_r)
					self.symbols[context_constant][var] = self.symbols[context_constant][cvar] * number(var_r)
#					self.symbols[cvar] = self.symbols[cvar] * (1 - number(var_r))

#					rint self.symbols

					cu_data.append(("eq", cvar, " * ".join([cvar, var_r])))
					context_var = var
					constant = self.symbols[context_constant][var]
					context = cu_context

					self.relational_var = cvar

#					rint "THIS", constant

					if container is not None:
						if self.containers is None:
							self.containers = {}

						if not container in self.containers:
							self.containers[container] = {}

						if not cu_k1 in self.containers[container]:
							self.containers[container][cu_k1] = {}

						if not context_constant in self.containers[container][cu_k1]:
							self.containers[container][cu_k1][context_constant] = {}

						self.containers[container][cu_k1][context_constant][cu_k2] = cu_data
						self.digest_unit_groups(container, cu_k1, context_constant, cu_k2)
				else:
					if context not in self.data:
						self.data[context] = {}

					if unit not in self.data[context]:
						self.data[context][unit] = []

					if var_r is not None:
						raise Exception("Handle me")

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
					data.append(("eqx", sym, None))
					if not osym in self.work:
						self.work[osym] = []
					self.work[osym].append("= " + str(sym))

			if target:
				if self.containers is None:
					self.containers = {}
				if not container in self.containers:
					self.containers[container] = {}
				if not target in self.containers[container]:
					self.containers[container][target] = {}
				if not target_constant in self.containers[container][target]:
					self.containers[container][target][target_constant] = {}
				if not unit in self.containers[container][target][target_constant]:
					self.containers[container][target][target_constant][unit] = []
				self.containers[container][target][target_constant][unit].append(("ad", constant, context_var))

			# we subtract from the context owner and give to the target
			if operator == "ex":
				operator = "su"

			#if not answer_out:
			data.append((operator, constant, context_var))

			if zeroes_out:
				data.append(("ans", "0", None))
			if answer_out:
				data.append(("ans", constant, None))

		# If nothing was done there's nothing to do
		if len(data) == 0:
			self.data = None
			self.actor_data = None
			self.containers = None

		if container is not None:
			if self.containers is None:
				self.containers = {}

			if not container in self.containers:
				self.containers[container] = {}

			if not k1 in self.containers[container]:
				self.containers[container][k1] = {}

			if not context_constant in self.containers[container][k1]:
				self.containers[container][k1][context_constant] = {}

			self.containers[container][k1][context_constant][k2] = data
			#rint "==="
			#rint "WAT", container, k1, context_constant, k2, data
			#rint self.containers
			self.digest_unit_groups(container, k1, context_constant, k2)

		if self.coordinated:
#			rint self.coordinated_container, container
			if self.coordinated_container[0] != container:
				cc = self.coordinated_container
				if not cc[1] in self.containers[container]:
					self.containers[container][cc[1]] = {}
				if not context_constant in self.containers[container][cc[1]]:
					self.containers[container][cc[1]][context_constant] = {}
				self.containers[container][cc[1]][cc[2]][cc[3]] = self.containers[cc[0]][cc[1]][cc[2]][cc[3]]
				del self.containers[cc[0]][cc[1]][cc[2]][cc[3]]
				self.digest_unit_groups(container, cc[1], cc[2], cc[3], cc[0])
#			rint self.coordinated_container, container

		self.reset_extractor()
		return (container, k1, context_constant, k2)

	def digest_unit_groups(self, container, k1, context_constant, k2, rmc=None):
		data = None
		if container in self.containers:
			x = self.containers[container]
			if k1 in x:
				x = x[k1]
				if context_constant in x:
					x = x[context_constant]
					if k2 in x:
						data = x[k2]
		if data is not None:
			if not k2 in self.descriptive_units:
				if " " in k2:
					self.did_combine_units = True
					parts = k2.split(" ")

					# The item is the last part of the unit
					item = parts.pop()
					for part in parts:
						nu = " ".join([part, item])

						if nu in self.containers[container][k1][context_constant]:
							ndata = []
							# Format the data, changing any equivalence relationships
							# to additive ones, assuming we're starting with a 0 group
							# and then adding any numbers to it
							for da in data:
								x = da[0]
								if x == "eq":
									x = "ad"
								ndata.append((x, da[1], da[2]))
							self.containers[container][k1][context_constant][nu] += ndata
						else:
							self.containers[container][k1][context_constant][nu] = [] + data
						if rmc is not None:
							if rmc in self.containers:
								if k1 in self.containers[rmc]:
									if context_constant in self.containers[rmc][k1]:
										if nu in self.containers[rmc][k1][context_constant]:
											del self.containers[rmc][k1][context_constant][nu]

	def has_any(self):
		return self.container is not None or self.context is not None or self.operator is not None or self.constant is not None or self.unit is not None or self.context_unit is not None

	def has_all(self):
		b = self.unit is not None or self.context_unit is not None
		a = self.container is not None and self.context is not None and self.operator is not None and self.constant is not None and b

		if self.relative:
			if not self.comparator_context:
				return False

		return a

	def execute(self):
		p = self.problem
		i = p.inference

		self.last_index = len(i.sentences) - 1

		for parser in i.sentences:
			self.units = parser.units
			self.descriptive_units = parser.problem.descriptive_units
			# Sometimes one context will transfer to another. In those cases
			# we only want to change the context to the primary one
			did_set_context = False
			last_context = None
			last_context_subtype = None
			open_conjunction = False
			last_target = None
			last_target_subtype = None
			pending_constant = None
			last_container = None
			zeroes_out = False
			answer_out = False
			self.coordinated = False
			last_part = None
			for v_part in parser.parsed:
				val, part, subtype = v_part

				if subtype and subtype[0] == "self":
					val = self.problem.brain.self_reflexive(val, True)

				if part in ["context", "context_inferred"]:
					if not did_set_context:
						did_set_context = True
						self.context = val
						self.context_subtype = subtype
					elif self.can_target:
						self.target = val
						self.target_subtype = subtype
						last_target = val
						last_target_subtype = subtype
					last_context = val
					last_context_subtype = subtype
					if last_part == "constant" and not val in self.problem.units_acting_as_context:
						self.context_constant = self.constant
						self.uses_context_constant = True
						self.constant = None

				# Exestential operator
				if part == "exestential" and not self.operator:
					self.ex_op = True
					self.operator = "eq"

				if part == "operator" and not self.operator:
					self.operator = parser.operator[val]
					if self.operator == "co":
						self.operator = None
					if self.operator == "ex":
						self.can_target = True

				if part == "constant":
					if not self.constant:
						self.constant = val
					elif open_conjunction:
						pending_constant = val

				if part == "variable_relationship":
					self.variable_relationship = val

				if part == "unit":
					if open_conjunction and pending_constant:
						if self.has_any():
							self.coordinated_container = self.generate_expression(zeroes_out, answer_out)
							self.constant = pending_constant
							pending_constant = None

							self.coordinated = True
							self.context = last_context
							self.context_subtype = last_context_subtype
							self.container = last_container
							did_set_context = False
					self.unit = val

				if part == "context_unit":
					self.context_unit = val

				if part == "solution_zero":
					zeroes_out = True
					self.zeroes_out = True

				if part in "rel_less":
					self.rel_mode = "su"
					self.relative = True

				if part in "rel_more":
					self.rel_mode = "ad"
					self.relative = True

				if part in "asking":
					self.asking = True

				if part == "comparator_context":
					if self.can_target:
						self.target = val[0]
						self.target_subtype = subtype
						last_target = val[0]
						last_target_subtype = subtype
					else:
						self.comparator_context = val[0]

				if part == "pre_ind_plu":
					if last_context and not self.actor:
						self.actor = last_context
						last_context = None
						last_context_subtype = None

				if part == "acting":
					if self.actor:
						self.action = val

				if part in ["subordinate", "subordinate_inferred"]:
					open_conjunction = False
					pending_constant = None
					if val[1] is not None:
						if val[0] not in parser.subordinate_lookup:
							continue
						stype = parser.subordinate_lookup[val[0]]
						if self.constant is not None and stype in ["time_ending", "unit_requirement"]:
							answer_out = True
							self.answer_out = True
						else:
							# If we have a conjunction we have an container
							self.container = val[0]
							last_container = self.container

				if part == "conjunction":
					open_conjunction = True

				if part == "coordinating_conjunction":
					if self.has_any():
						self.coordinated_container = self.generate_expression(zeroes_out, answer_out)
					else:
						self.reset_extractor()

					#rint "Restore context and container"
					self.coordinated = True
					self.context = last_context
					self.context_subtype = last_context_subtype
					self.container = last_container
					did_set_context = False

				if self.has_all():
					#rint "Here and", zeroes_out
					self.generate_expression(zeroes_out, answer_out)
				last_part = part

				# @TODO: DEBUG
				#rint val
				#rint part
				#rint subtype
				#rint "----"

			if self.has_any():
				self.generate_expression(zeroes_out, answer_out)
			else:
				self.reset_extractor()

			#rint "CONTOUT", self.containers

			if self.containers is not None:
				self.sentence_data.append(self.containers)
				self.data = None
				self.actor_data = None
				self.containers = None

	def newvar(self, context_constant):
		sym = self.varpool.pop(0)
		self.used_vars.append(sym)
		self.symbols[context_constant][sym] = Symbol(sym)
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
#				rint "==="
#				rint sd
#				rint self.symbols
#				rint "--"
				#rint data
				new_data = {}
				for context in data:
					new_constant_wrapper = {}
					for context_constant in data[context]:
						units = data[context][context_constant]

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
								operator, constant, dc = values

								symref = dc
								if not context_constant in self.symbols:
									self.symbols[context_constant] = {}

								if constant in self.symbols[context_constant]:
									if symref is None:
										symref = constant
									constant = self.symbols[context_constant][constant]
								elif constant is not None:
									if isinstance(constant, basestring):
										# Convert and type the constant properly
										constant = number(constant)

								# Apply the operation to the symbol
								if operator is not None:
									inf, symbol, con, sym = self.get_symbol(context, context_constant,
											unit, container, index, operator, constant, False, symref)
								#	if inf:
								#		new_values.append(("eq", "0"))
								else:
									con = constant
								#	rint "HERE THEN?", con, constant
								#rint "DIS", new_values, unit, context_constant, context, container
								new_values.append((operator, con, dc))
							new_units[unit] = new_values
						new_constant_wrapper[context_constant] = new_units
						last_context = context
					new_data[context] = new_constant_wrapper
					#rint context, new_constant_wrapper, container
				new_container[container] = new_data
			index += 1
			new_sentence_data.append(new_container)
		self.sentence_data = new_sentence_data
		#rint self.sentence_data

	def compute_correct(self):
		self.compute()

		p = self.problem
		i = p.inference
		q = p.question

		def format_response_value(val):
			val = str(simplify(val))
			if self.sig_figs == -1:
				if "." in val:
					val = str(float(val))
					if val[-2:] == ".0":
						val = val[:-2]
			return val

		def add_response(val, unit, idx):
			for v in val:
				i = [format_response_value(v)]
				if unit is not None:
					i.append(unit)
				self.correct_responses.insert(idx, " ".join(i))

		def safe_solve(*args):
			try:
				return solve(*args)
			except Exception as e:
				print str(e)
				return None

		def simple_solve(sym, context_constant, rel_var=None):
			solve_for = sym
			if context_constant is None:
				context_constant = "_unknown_"

			if self.relational_var is not None:
				solve_for = self.symbols[context_constant][self.relational_var]

			did_match = False
			for c in [Symbol, Function, Pow, Derivative]:
				if isinstance(sym, c):
					did_match = True
					return safe_solve(sym, solve_for)

			return [sym]

		index = 0
		for answer in q.answers:
			needEqu = True
			dispSym = None
			if answer.actor and answer.action:
				needEqu = False
				# The answer in actor/action questions is the actor normally?
				answer.unit = answer.actor
				inf, equ, con, sym = self.get_symbol("@" + answer.actor, answer.context_constant, answer.action, None, index)

			resp = None
			dontSave = False
			compContext = None

			#rint self.symbols
			#rint self.ending_vars
			#rint self.beginning_vars

			#rint answer.subordinates, answer.unit, answer.context
			#rint answer.actor, answer.action

			if len(answer.subordinates) > 0:
				working_answer = None
				for s in answer.subordinates:
					word, sub = s

					if sub == "context_grouping" and answer.context is None and self.problem.exestential:
						# Exestential problems may not have contexts for things
						# wonder about alltogetherness. This is a tough case
						# to handle, so the solution is simply to ignore that
						# we have a context grouping assignment and instead
						# transit the subtype over to the 'unit_grouping' mode
						sub = "unit_grouping"

					if sub == "time_ending":
						l = len(self.ending_vars)

						if needEqu:
							inf, equ, con, sym = self.get_symbol(answer.context, answer.context_constant, answer.unit, None, index)

						if l == 1:
							symbol = self.symbols[answer.context_constant][self.ending_vars[0]]
							resp = (safe_solve(equ, symbol), answer.unit)
						elif l == 0:
							if self.symbol_answer and sym:
								resp = (safe_solve(equ, Symbol(sym)), answer.unit)
							else:
								resp = (simple_solve(equ, answer.context_constant), answer.unit)
						else:
							self.correct_responses.append(
								"Not sure; too many ending variables!")
					elif sub == "time_starting":
						l = len(self.beginning_vars)
						if needEqu:
							inf, equ, con, sym = self.get_symbol(answer.context, answer.context_constant, answer.unit, None, index)
						if l == 1:
							name, symbol = self.beginning_vars[0]
							resp = (safe_solve(equ, symbol), answer.unit)
						elif l == 0:
							if self.symbol_answer and sym:
								resp = (safe_solve(equ, Symbol(sym)), answer.unit)
							else:
								resp = (simple_solve(equ, answer.context_constant), answer.unit)
						else:
							self.correct_responses.append(
								"Not sure; too many starting variables!")
					elif sub == "unit_grouping":
						if not self.did_combine_units:
							self.correct_responses.append("Not sure; don't know how to handle grouped units that aren't combined")
						# As of now, units are grouped ahead of time, so this
						# should be a virtual solution having already compiled
						# the units ahead of time
					elif sub == "context_grouping":
						ans = 0
						syms = []
						if answer.context in self.problem.adaptive_context:
							for c in self.problem.adaptive_context[answer.context]:
								context, context_subtype = c
								sinf, sequ, scon, ssym = self.get_symbol(context, answer.context_constant, answer.unit, None)
								self.work[ssym].append("= " + " + ".join(syms))
								syms.append(ssym)
								ans += sequ
						resp = (simple_solve(ans, answer.context_constant), answer.unit)
					elif sub == "unit_requirement":
						pass
						# This should get handled in the formal logic elsewhere
					elif sub == "place_noun" or sub is None:
						#rint "here?"
						compContext = word
						dispUnit = answer.unit
						if answer.actor:
							if answer.action:
								inf, equ, con, sym = self.get_symbol("@" + answer.actor, answer.context_constant, answer.action, word, index)
							else:
								inf, equ, con, sym = self.get_symbol(answer.context, answer.context_constant, answer.actor, word, index)
								dispUnit = answer.actor
						else:
							inf, equ, con, sym = self.get_symbol(answer.context, answer.context_constant, answer.unit, word, index)
						#rint inf, equ, con, sym
						resp = (simple_solve(equ, answer.context_constant), dispUnit)
					elif sub == "comparator":
						pass
					else:
						dontSave = True
						self.correct_responses.append("Not sure; unknown subordinate type {0} ({1})".format(sub, word))
			else:
				if needEqu:
					inf, equ, con, sym = self.get_symbol(answer.context, answer.context_constant, answer.unit, None, index)

				if self.uses_context_constant is not None:
					if answer.context_constant > 1:
						singleForm = self.problem.brain.raw["word_forms"]["single"][answer.context]
						if not singleForm:
							raise Exception("FIX THIS")
						else:
							s_inf, s_equ, s_con, s_sym = self.get_symbol(singleForm, "1", answer.unit, None, index)
							if s_inf and s_con is None:
								raise Exception("FIX: No definition for single context constant")
							else:
								# We have the definition for a single context
								# so we can simply apply it
								equ = (s_equ * number(answer.context_constant))
				resp = (simple_solve(equ, answer.context_constant), answer.unit)

			if answer.relative:
				inf, equ, con, sym = self.get_symbol(answer.context, answer.context_constant, answer.unit, None, index)
				if answer.comparator is not None:
					coinf, comp, conc, csym = self.get_symbol(answer.comparator, answer.context_constant, answer.unit, compContext)
				elif answer.comparator_unit is not None:
					coinf, comp, conc, csym = self.get_symbol(answer.context, answer.context_constant, answer.comparator_unit, compContext)
				else:
					coinf, comp, conc, csym = self.get_symbol(answer.context, answer.context_constant, answer.unit, None)

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

				#rint self.symbols, answer.rel_mode, r, comp, answr.context

				if self.symbol_answer and csym:
					resp = (safe_solve(equ, Symbol(csym)), answer.unit)
				else:
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

					# putting more and less in the answer is questionable
					#if answer.unit:
					#	unt.insert(0, answer.unit)

					#resp = (simple_solve(v), " ".join(unt))
					resp = (simple_solve(v, answer.context_constant), answer.unit)

			if resp[0] is None:
				dontSave = True

			if not dontSave:
				r, u = resp
				#rint r, u, resp
				if self.zeroes_out:
					self.work[sym].append("= 0")
				add_response(r, u, index)

			index += 1

	def __str__(self):
		o = []

		o.append("\n## Data extraction")
		index = 1
		#rint dumps(self.sentence_data, indent=4, sort_keys=True)
		for sd in self.sentence_data:
			b = []
			for container in sd:
				data = sd[container]
				s = []
				for context in data:
					for context_constant in data[context]:
						if context is None:
							context = "_unknown_"
						#rint context, unit, data
						units = data[context][context_constant]
						for unit in units:
							for values in units[unit]:
								operator, constant, dc = values
								i = []

								actor = None
								action = None
								context_unit = None
								target = None

								if context is not None and context[0:1] == "@":
									actor = context[1:]
									action = unit
									unit = None
									context = None

								if context == "_unknown_":
									context = None

								if context_constant == "_unknown_" or context_constant is None:
									context_constant = None
								else:
									context = " ".join([context_constant, context])

								if unit == "_unknown_":
									unit = None

								if container is None or container == "_unknown_":
									container = None
								elif container in self.problem.inference.subordinate_strings:
									container = self.problem.inference.subordinate_strings[container]

								display_constant = dc
								if dc is None:
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
									if target:
										i.append(target)
										i.append("=")
									i.append(display_constant)
								elif context is not None and unit is not None:

									i.append(unit)
									if operator is not None and operator == "re":
										i.append("needed by")
									else:
									#	i.append(OPERATOR_STR[operator])
										i.append("owned by")

#									if self.problem.inference.is_requirement_problem:

									i.append(context)

									if container is not None and container:
										i.append(container)

									i.append(OP_DISPLAY[operator])

									if target:
										i.append(target)
										i.append("=")

									i.append(display_constant)
								elif context is None and unit is not None and self.problem.exestential:
									i.append(unit)

									if container is not None:
										i.append(container)

									i.append(OP_DISPLAY[operator])
									if target:
										i.append(target)
										i.append("=")

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
		#rint self.symbols

		return "\n".join(o)
