#!/usr/bin/env python
"""Zoidberg Standard Interpreter

Adds interpretation to a provided Problem object.
"""
import inferences as infer
import converter as convert
from thinker import Thinker
from definitions import Operation, Relation
from statement import Statement
from expression import Expression
from term import Term
from sympy import Symbol

class Interpretation(Thinker):
	def __init__(self, problem):
		super(Interpretation, self).__init__()
		# Operation flags
		self.build_expression = None

		# Current state
		self.last_value = None
		self.last_operation = None
		self.last_relation = None

		# Output
		self.expression = None
		self.statement = None

		# Variables
		self.variable_str = "zoid_{0}"
		self.variable_uid = 0

		# Statements for working on
		self.statements = []

		# Information required to answer
		self.solution_unit = None
		self.solution_context = None

		# Begin the interpretation
		for sentence_tags in problem.sentence_tags:
			for t in sentence_tags:
				self._interpret(*t)
		self._analyze()

	# Analysis
	def _analyze(self):
		if not self.statement:
			self._think("No statement created.")
			if self.expression:
				self._create_statement("of assumed equality.")
			self.last_relation = Relation.EQUIVALENCE
			self._handle_relation()

		is_equivalence = self.statement.relation == Relation.EQUIVALENCE
		if is_equivalence and len(self.statement.expressions) == 1:
			if self.expression:
				self._think("Adding current expression to statement.")
				self._add("expression")
			else:
				self._create_expression("for hanging equality.")
				self._set_variable()
				self._add("expression")
			self._add("statement")

	# Output
	def _create_statement(self, reasoning):
		self._think("New statement {0}", reasoning)
		self.statement = Statement()

	def _create_variable(self):
		var = self.variable_str.format(self.variable_uid)
		self._think("'{0}' is a value (a variable).", var)
		v = Symbol(var)
		self.variable_uid += 1
		return v

	def _create_expression(self, reasoning):
		self._think("New expression {0}", reasoning)
		self.expression = Expression()
		self._handle_relation()

	# Handlers
	def _handle_relation(self):
		if self.last_relation:
			if not self.statement:
				self._create_statement("for relationship.")
			self._add("expression")
			self._add("last_relation")

	# Expression building
	def _add_term(self, term):
		if self.build_expression and not self.expression:
			self._create_expression("for new term")
		self.expression.terms.append(term)

	def _add(self, v):
		val = getattr(self, v)
		setattr(self, v, None)
		if v == "expression":
			self.statement.expressions.append(val)
			return

		if v == "statement":
			self.statements.append(val)
			return

		if v == "last_relation":
			self.statement.relation = val
			return

		if v == "last_value":
			t = Term(Term.VALUE, val)
		if v == "last_operation":
			t = Term(Term.OPERATION, val)
		self._think("Adding term '{0}' to current expression.", str(t))
		self._add_term(t)

	# States
	def _set_variable(self, name=None):
		if name:
			self._think("'{0}' is a value (a variable).", name)
			v = Symbol(name)
		else:
			v = self._create_variable()
		self.last_value = v
		if self.build_expression:
			self._add("last_value")

	def _set_constant(self, v):
		v = convert.to_number(v)
		self._think("'{0}' is a value (a constant).", v)
		self.last_value = v
		if self.build_expression:
			self._add("last_value")

	def _set_relation(self, v):
		v = convert.to_relation(v)
		self.last_relation = v
		self._think("'{0}' is a relationship.", v)

		if self.expression:
			self._handle_relation()

	def _set_operation(self, v):
		v = convert.to_operation(v)
		self.last_operation = v
		self._think("'{0}' is an operation.", v)

		if self.last_value:
			if not self.expression:
				self._create_expression("indicated by value and operation.")

		if self.build_expression is None:
			self.build_expression = True
			self._assume("the beginning of a simple expression.")

		if self.last_value:
			self._add("last_value")
		self._add("last_operation")

	# Support
	def _interpret(self, word, tag):
		if word.isalpha():
			self._think("{0} is alpha", word)
			if self.build_expression:
				self._set_variable(word)
		else:
			if infer.is_number(word):
				self._set_constant(word)
			if infer.is_relation(word):
				self._set_relation(word)
			if infer.is_operation(word):
				self._set_operation(word)
