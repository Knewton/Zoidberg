#!/usr/bin/env python
"""Zoidberg Solution

Uses a problem's interpretation to solve it.
"""
from thinker import Thinker
from definitions import Relation, Operation
from term import Term
from sympy import Eq, Rational
from sympy.solvers import solve
from copy import copy

class Solution(Thinker):
	def __init__(self, problem):
		# Thought log
		self.thoughts = []

		# The answer
		self.answer = None

		# Begin the solution
		self._solve_problem(problem)

	# Types of solvers
	def _solve_equivalence_statement(self, s):
		expressions = s.expressions
		self._think("Solving equivalence statement")
		a = self._solve_expression(expressions[0])
		b = self._solve_expression(expressions[1])
		self._think("I think a = {0}", a)
		self._think("I think b = {0}", b)
		soln = solve(Eq(a, b))

		# solution returned as an array of answers or an object
		if len(soln) == 1:
			try:
				return soln[0]
			except KeyError:
				return soln
		else:
			return soln

	# Solvers
	def _solve_expression(self, e):
		ops = e.operations()
		terms = copy(e.terms)
		for op in Operation.ALL:
			if op in ops:
				new_terms = []
				pending_operation = None
				for t in terms:
					if t.type is Term.OPERATION:
						pending_operation = t.value
					elif pending_operation is not None:
						new_terms.append(Operation.do(pending_operation,
														new_terms.pop().value,
														t.value))
						pending_operation = None
					else:
						new_terms.append(t)
				terms = new_terms
		if len(terms) == 1:
			return terms[0].value

	def _solve_statement(self, s):
		solution = None
		try:
			if s.relation == Relation.EQUIVALENCE:
				solution = self._solve_equivalence_statement(s)
			return solution
		except Exception as e:
			self._think("Something bad happened: {0}", e)

		if solution is None:
			self._think("I don't know how to solve this statement")
			return None

	def _solve_problem(self, problem):
		statements = problem.interpretation.statements
		if len(statements) == 1:
			self._think("Solving the problem")
			solution = self._solve_statement(statements[0])
			if solution is not None:
				self.answer = solution
				self._think("I think I solved the problem")
		else:
			self._think("I don't know how to solve this problem")
