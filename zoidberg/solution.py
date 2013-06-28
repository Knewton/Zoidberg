#!/usr/bin/env python

from sympy import Symbol, Function, Derivative
from sympy.core.power import Pow
from sympy import Eq, Rational
from sympy.solvers import solve

OP_DISPLAY = {
	"ans": "==",
	"eq": "=",
	"ad": "+",
	"mu": "*",
	"su": "-",
	"di": "/"
}

def number(s):
	return float(s) if '.' in s else int(s)

class Solution(object):
	def __init__(self, problem):
		self.problem = problem
		self.last_index = 0

		self.context = None
		self.operator = None
		self.constant = None
		self.unit = None
		self.comparator_context = None
		self.relative = False
		self.rel_mode = None

		self.sentence_data = []
		self.data = None
		letters = [chr(x) for x in xrange(ord("a"), ord("z")+1)]
		self.varpool = letters[-3:] + letters[:-3]

		self.beginning_vars = []
		self.middle_vars = []
		self.ending_vars = []

		self.used_vars = []
		self.symbols = {}
		self.correct_responses = []

		self.execute()

	def store_var(self, idx, var):
		if idx == 0:
			self.beginning_vars.append(var)
		elif idx == self.last_index:
			self.ending_vars.append(var)
		else:
			self.middle_vars.append(var)

	def get_symbol(self, context, unit, idx=-1, operator=None, constant=None):
		sym = " ".join([context, unit])
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

		if constant is None:
			var = self.newvar()
			constant = self.symbols[var]
			if hindsight_inference:
				self.store_var(idx, var)
		else:
			var = str(constant)

		if operator is not None and constant is not None:
			if operator == "eq":
				self.store_var(idx, sym)
				symbol = constant
			elif operator == "ad":
				symbol += constant
			elif operator == "su":
				symbol -= constant
			elif operator == "mu":
				symbol *= constant
			elif operator == "di":
				symbol /= constant
			else:
				return (hindsight_inference, symbol, var)
			self.symbols[sym] = symbol

		return (hindsight_inference, symbol, var)

	def reset_extractor(self):
		self.context = None
		self.operator = None
		self.constant = None
		self.unit = None
		self.comparator_context = None
		self.relative = False
		self.rel_mode = None

	def generate_expression(self, zeroes_out=False):
		if self.data is None:
			self.data = {}

		context = self.context
		operator = self.operator
		constant = self.constant
		unit = self.unit

		if context is None:
			context = "_unknown_"

		if unit is None:
			unit = "_unknown_"

		if context not in self.data:
			self.data[context] = {}

		if unit not in self.data[context]:
			self.data[context][unit] = []

		if self.relative and self.comparator_context:
			sym = " ".join([self.comparator_context, unit])
			if operator == "eq":
				operator = self.rel_mode
				self.data[context][unit].append(("eq", sym))

		self.data[context][unit].append((operator, constant))
		if zeroes_out:
			self.data[context][unit].append(("ans", "0"))
		self.reset_extractor()

	def has_any(self):
		return self.context or self.operator or self.constant or self.unit

	def has_all(self):
		a = self.context and self.operator and self.constant and self.unit
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
			zeroes_out = False
			for v_part in parser.parsed:
				val, part, subtype = v_part

				if part == "context":
					if not did_set_context:
						did_set_context = True
						self.context = val

				if part == "operator":
					self.operator = parser.operator[val]

				if part == "constant":
					self.constant = val

				if part == "unit":
					self.unit = val

				if part == "solution_zero":
					zeroes_out = True

				if part in "rel_less":
					self.rel_mode = "su"
					self.relative = True

				if part in "rel_more":
					self.rel_mode = "ad"
					self.relative = True

				if part == "comparator_context":
					self.comparator_context = val[0]

				if self.has_all():
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

			if self.data is not None:
				self.sentence_data.append(self.data)
				self.data = None

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
		for data in self.sentence_data:
			new_data = {}
			for context in data:
				units = data[context]

				# Use the last context for inclusive context
				if p.brain.is_inclusive(context):
					if last_context is not None:
						context = last_context
						switch_context = True
					else:
						# @TODO: This state should probably never happen?
						# A context that is inclusive should have one context
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
							inf, symbol, con = self.get_symbol(context, unit,
									index, operator, constant)
							if inf:
								new_values.append(("eq", "0"))
						new_values.append((operator, con))
					new_units[unit] = new_values
				new_data[context] = new_units
				last_context = context
			index += 1
			new_sentence_data.append(new_data)
		self.sentence_data = new_sentence_data

	def compute_correct(self):
		self.compute()

		p = self.problem
		i = p.inference
		q = p.question

		def add_response(val, unit):
			for v in val:
				i = [str(v)]
				if unit is not None:
					i.append(unit)
				self.correct_responses.append(" ".join(i))

		def simple_solve(sym):
			for c in [Symbol, Function, Pow, Derivative]:
				if isinstance(sym, c):
					return solve(sym, sym)
			return [sym]

		for answer in q.answers:
			inf, equ, con = self.get_symbol(answer.context, answer.unit)
			if answer.subordinate is not None:
				if answer.subordinate == "time_ending":
					l = len(self.ending_vars)

					if l == 1:
						symbol = self.symbols[self.ending_vars[0]]
						add_response(solve(equ, symbol), answer.unit)
					elif l == 0:
						add_response(simple_solve(equ), answer.unit)
					else:
						self.correct_responses.append(
							"Not sure; too many ending variables!")
				elif answer.subordinate == "time_starting":
					if len(self.beginning_vars) == 1:
						symbol = self.symbols[self.beginning_vars[0]]
						add_response(solve(equ, symbol), answer.unit)
					elif l == 0:
						add_response(simple_solve(equ))
					else:
						self.correct_responses.append(
							"Not sure; too many starting variables!")
				else:
					self.correct_responses.append("No sure; no subordinates!")
			elif answer.relative:
				coinf, comp, conc= self.get_symbol(answer.comparator, answer.unit)

				v = self.newvar()
				v = 0

				# ad(dition): how many more
				if answer.rel_mode == "ad":
					v = equ - comp
					unt = ["more"]
				# su(btraction) how many fewer
				elif answer.rel_mode == "su":
					v = comp - equ
					unt = ["fewer"]

				if answer.unit:
					unt.append(answer.unit)

				add_response(simple_solve(v), " ".join(unt))
			else:
				add_response(simple_solve(equ), answer.unit)

	def __str__(self):
		o = []

		o.append("\n## Data extraction")
		index = 1
		for data in self.sentence_data:
			s = []
			for context in data:
				for unit in data[context]:
					for values in data[context][unit]:
						operator, constant = values
						i = []

						display_constant = constant
						if display_constant is None:
							display_constant = "<an unknown number>"

						if operator is None:
							continue # Probably the question

						if context != "_unknown_" and unit != "_unknown_":
							i.append(unit)
							i.append("owend by")
							i.append(context)
							i.append(OP_DISPLAY[operator])
							i.append(display_constant)
						else:
							i.append("I don't know how to format this state!")

						s.append(" ".join(i))

			if len(s) > 0:
				o.append("\n### Sentence {0}".format(index))
				o.append("\n".join(s))
			index += 1

		if len(self.correct_responses) > 0:
			o.append("\n## Correct response")
			index = 1
			for response in self.correct_responses:
				if len(self.correct_responses) > 1:
					o.append("\n### Response {0}".format(index))
				o.append(response)
				index += 1

		return "\n".join(o)
