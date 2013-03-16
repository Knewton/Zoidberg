#!/usr/bin/env python

from sympy import Symbol, Function, Derivative
from sympy.core.power import Pow
from sympy import Eq, Rational
from sympy.solvers import solve

OP_DISPLAY = {
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

		self.context = None
		self.operator = None
		self.constant = None
		self.unit = None
		self.sentence_data = []
		self.data = None

		self.symbols = {}
		self.correct_responses = []

		self.execute()

	def get_symbol(self, context, unit, operator=None, constant=None):
		sym = " ".join([context, unit])
		if sym not in self.symbols:
			self.symbols[sym] = Symbol(sym)

		symbol = self.symbols[sym]
		if operator is not None and constant is not None:
			if operator == "eq":
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
				return symbol
			self.symbols[sym] = symbol

		return symbol

	def reset_extractor(self):
		self.context = None
		self.operator = None
		self.constant = None
		self.unit = None

	def generate_expression(self):
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

		self.data[context][unit].append((operator, constant))
		self.reset_extractor()

	def has_any(self):
		return self.context or self.operator or self.constant or self.unit

	def has_all(self):
		return self.context and self.operator and self.constant and self.unit

	def execute(self):
		p = self.problem
		i = p.inference

		for parser in i.sentences:
			for v_part in parser.parsed:
				val, part, subtype = v_part

				if part == "context":
					self.context = val

				if part == "operator":
					self.operator = parser.operator[val]

				if part == "constant":
					self.constant = val

				if part == "unit":
					self.unit = val

				if self.has_all():
					self.generate_expression()

				# @TODO: DEBUG
				#print val
				#print part
				#print subtype
				#print "----"

			if self.has_any():
				self.generate_expression()
			else:
				self.reset_extractor()

			if self.data is not None:
				self.sentence_data.append(self.data)
				self.data = None

	def compute(self):
		index = 0
		for data in self.sentence_data:
			for context in data:
				for unit in data[context]:
					# We increment at the start because of the bail-out nature
					data_index = -1
					for values in data[context][unit]:
						data_index += 1
						operator, constant = values

						if constant is None:
							continue # Undefined valueis a no-op

						# Convert and type the constant properly
						constant = number(constant)

						# Apply the operation to the symbol
						if operator is None:
							continue # The answer probably; no-op
						else:
							self.get_symbol(context, unit, operator, constant)
			index += 1

	def compute_correct(self):
		self.compute()

		p = self.problem
		i = p.inference
		q = p.question

		def add_response(val, unit):
			i = [str(val)]
			if unit is not None:
				i.append(unit)
			self.correct_responses.append(" ".join(i))

		def simple_solve(sym):
			for c in [Symbol, Function, Pow, Derivative]:
				if isinstance(sym, c):
					return solve(sym, sym)
			return sym

		for answer in q.answers:
			symbol = self.get_symbol(answer.context, answer.unit)
			if answer.subordinate is not None:
				if answer.subordinate == "time_ending":
					add_response(simple_solve(symbol), answer.unit)
				else:
					self.correct_responses.append("No idea! Sorry!")
			else:
				self.correct_responses.append("No idea! Sorry!")

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
							display_constant = "some"

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
