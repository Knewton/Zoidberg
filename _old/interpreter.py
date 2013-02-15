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
from quirks import quirk_fix
from re import compile

ALPHA = compile("[A-Za-z]")

class Interpretation(Thinker):
	def __init__(self, problem):
		super(Interpretation, self).__init__()
		# Operation flags
		self.build_expression = None
		self.context_ownership = False

		# Current state
		self.last_tag = None
		self.last_value = None
		self.last_operation = None
		self.last_relation = None
		self.last_unit = None
		self.last_context = None
		self.primary_context = None

		# Output
		self.expression = None
		self.statement = None

		# Problem details
		self.units = []
		# A context is used to group pieces of expressions for comparison and
		# computation. For example "Jane gives Joe 3 apples" requires us to
		# know how many apples both "Jane" and "Joe" have. In this example,
		# "Jane" and "Joe" are both contexts which can 'own' some number of
		# a unit, in this case 'apples'.
		self.contexts = {}

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
			else:
				self._think("I don't know what to do.")
				return

		is_equivalence = self.statement.relation == Relation.EQUIVALENCE
		if is_equivalence and len(self.statement.expressions) == 1:
			if self.expression:
				self._think("Inserting current expression to statement.")
				self._add("expression")
			else:
				self._create_expression("for hanging equality.")
				self._set_variable()
				if not self.build_expression:
					self._add("last_value")
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

	def _create_context(self, context):
		if not context in self.contexts:
			self._think("New context '{0}'", context)
			self.contexts[context] = {}

	def _rename_context(self, context, newname):
		if context in self.contexts:
			self._think("Context '{0}' becomes '{1}'", context, newname)
			self.contexts[newname] = self.contexts[context]
			del self.contexts[context]
			if context == self.primary_context:
				self._think("Renaming primary context to '{0}'", newname)
				self.primary_context = newname

	def _create_unit(self, unit):
		if not unit in self.units:
			self._think("New unit '{0}'", unit)
			self.units.append(unit)

	# Handlers
	def _handle_unit_context(self):
		if self.last_context and self.last_unit:
			if self.context_ownership and self.last_value:
					c = self.contexts[self.last_context]
					if not self.last_unit in c:
						if not self.expression:
							self._think("This isn't a simple expression")
							self.build_expression = False
							self._create_expression(
								"for {0} owned by {1}".format(
									self.last_unit, self.last_context))
							c[self.last_unit] = self.expression
					else:
						self._add("last_value")

	def _handle_relation(self):
		if self.last_relation:
			if not self.statement:
				self._create_statement("for relationship.")
			self._add("expression")
			self._add("last_relation")

	def _handle_tag(self, tag, word):
		tag, word, thought = quirk_fix(tag, word)
		if thought is not None:
			self._think(thought)

		if tag in ["NNP", "NN"]: # noun, proper, singular, common
			self._think("I think '{0}' is a context", word)
			if self.last_tag == tag:
				context = "{0} {1}".format(self.last_context, word)
				self._rename_context(self.last_context, context)
				self.last_context = None
				self._set_context(context)
			else:
				self._create_context(word)
				self._set_context(word)

		if tag == "NNS": #noun, common, plural
			if self.last_value and not self.last_unit:
				self._think("I think '{0}' is a unit", word)
				self._create_unit(word)
			if word in self.units:
				self._set_unit(word)

		if tag in ["VBZ", "VBD"]: # verb, present tense, past tense
			if self.last_context:
				if infer.conveys.ownership(word):
					self._think("I think '{0}' conveys ownership", word)
					self.context_ownership = True
				elif infer.is_operation(word):
					self._think("I think '{0}' conveys an operation", word)
					self._set_operation(word)

		if tag in ["PRP", "PRP$"]: # pronoun, personal
			if self.last_context:
				self._think("I think '{0}' refers to '{1}'", word,
					self.last_context)

		if tag == "DT": # determiner
			self._think("I think '{0}' is a determiner.", word)
			if infer.is_operation(word):
				self._think("I think '{0}' is an operation; skipping.", word)
			if infer.conveys.variable(word):
				self._set_variable(word)

		if tag == ".":
			if self.last_context != self.primary_context:
				self._think("Resetting context to '{0}'", self.primary_context)
				self.last_context = self.primary_context

		self.last_tag = tag

	# Expression building
	def _add_term(self, term):
		if self.build_expression and not self.expression:
			self._create_expression("for new term")
		self.expression.terms.append(term)

	def _clear(self, v):
		setattr(self, v, None)

	def _add(self, v):
		val = getattr(self, v)
		self._clear(v)
		if val is None:
			return

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
		self._think("Inserting term '{0}' to current expression.", str(t))
		self._add_term(t)

	# States
	def _set_context(self, context):
		if not self.primary_context:
			self._think("Setting primary context to '{0}'", context)
			self.primary_context = context

		if not self.last_context:
			self._think("Setting current context to '{0}'", context)
			self.last_context = context
			self._handle_unit_context()
		else:
			self._think("Switching context to '{0}'", context)
			self._handle_unit_context()
			self.last_context = context

	def _set_unit(self, unit):
		if not self.last_unit:
			self._think("Setting current unit to '{0}'", unit)
			self.last_unit = unit
		elif self.last_unit == unit:
			self._think("We continue to work with unit '{0}'", unit)
		self._handle_unit_context()

	def _set_variable(self, name=None, context=None):
		if name:
			if context:
				name = "{0}_{1}".format(context, name)
			self._think("'{0}' is a value (a variable).", name)
			v = Symbol(name)
		else:
			v = self._create_variable()
		self.last_value = v
		if self.build_expression or self.expression:
			self._add("last_value")

	def _set_constant(self, v):
		v = convert.to_number(v)
		self.last_value = v
		if self.build_expression or self.expression:
			self._add("last_value")

	def _set_relation(self, v):
		v = convert.to_relation(v)
		self.last_relation = v

		if self.expression:
			self._handle_relation()

	def _set_operation(self, v):
		v = convert.to_operation(v)
		self.last_operation = v

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
		if ALPHA.match(word) or tag == ".":
			if self.build_expression:
				self._set_variable(word)
			else:
				self._handle_tag(tag, word)
		else:
			if infer.is_number(word):
				self._think("'{0}' is a value (a constant).", word)
				self._set_constant(word)
			if infer.is_relation(word):
				self._think("'{0}' is a relationship.", word)
				self._set_relation(word)
			if infer.is_operation(word):
				self._think("'{0}' is an operation.", word)
				self._set_operation(word)
