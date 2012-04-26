#!/usr/bin/env python
from argparse import ArgumentParser, FileType
from sys import exit, stdout
from re import compile
from nltk.data import load
from nltk import word_tokenize, pos_tag
from sympy.solvers import solve
from sympy import Symbol, Eq
from copy import copy

# Enums
class Operation:
	ADDITION="+"
	SUBTRACTION="-"
	MULTIPLICATION="*"
	DIVISION="/"
	ALL=["*", "/", "+", "-"]
	TESTER=[
		"*",
		"/",
		"+",
		"-"
	]

	@staticmethod
	def do(op, t1, t2):
		if op == "+":
			result = t1 + t2
		if op == "-":
			result = t1 - t2
		if op == "*":
			result = t1 * t2
		if op == "/":
			result = t1 / t2
		return Term(Term.VARIABLE, result)

class Relation:
	EQUIVALENCE="="
	ALL=["="]
	TESTER=["="]

# Representations
class Term(object):
	VARIABLE="var"
	OPERATION="op"
	FUNCTION="func"

	def __init__(self, type, value):
		self.type = type
		self.value = value

	def __str__(self):
		return str(self.value)

class Expression(object):
	def __init__(self, terms=None):
		self.terms = terms if terms is not None else []

	def add(self, term):
		self.terms.append(term)

	def operations(self):
		return list(set([o.value for o in self.terms
									if o.type is Term.OPERATION]))

	def solve(self):
		ops = self.operations()
		terms = copy(self.terms)
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

	def __str__(self):
		return "{0}".format(" ".join([str(t) for t in self.terms]))

class Statement(object):
	def __init__(self):
		self.expressions = []
		self.relation = None
		self.solve_vars = []

	def add(self, exp):
		if len(self.expressions) == 2:
			raise Exception("Malformed statement")
		else:
			self.expressions.append(exp)

	def relate(self, relation):
		self.relation = relation

	def solve_for(self, var):
		self.solve_vars.append(var)

	def solve(self):
		e = self.expressions
		if len(e) < 2:
			raise Exception("Malformed statement")

		if self.relation == Relation.EQUIVALENCE:
			f = self.solve_vars
			if len(f) is 0:
				soln = solve(Eq(e[0].solve(), e[1].solve()))
			else:
				soln = solve(Eq(e[0].solve(), e[1].solve()), f)
			if len(soln) == 1:
				try:
					return soln[0]
				except KeyError:
					# For object-based resposnes
					return soln
			else:
				return soln

	def __str__(self):
		e = self.expressions
		if len(e) < 2:
			return "Malformed statement"
		else:
			return "{0} {1} {2}".format(e[0], self.relation, e[1])

# Testers
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def is_operation(s):
	return s in Operation.TESTER

def is_relation(s):
	return s in Relation.TESTER

# Interpreters
def to_number(s):
	return float(s) if '.' in s else int(s)

def to_operation(s):
	if s == "+":
		return Operation.ADDITION
	if s == "-":
		return Operation.SUBTRACTION
	if s == "*":
		return Operation.MULTIPLICATION
	if s in ["/", chr(247)]:
		return Operation.DIVISION

def to_relation(s):
	if s == "=":
		return Relation.EQUIVALENCE

# Parsers
def parse_word(word):
	if is_number(word):
		return Term(Term.VARIABLE, to_number(word))

	if is_operation(word):
		return Term(Term.OPERATION, to_operation(word))

	if is_relation(word):
		return Relation.EQUIVALENCE

	return Term(Term.VARIABLE, Symbol(word))

def parse_proposition(sentences):
	statements = []
	statement = Statement()
	expression = Expression()

	for sentence in sentences:
		for word in word_tokenize(sentence):
			r = parse_word(word)

			if is_relation(r):
				# assume a relationship as a break for expressions
				statement.add(expression)
				expression = Expression()

				if statement.relation is not None:
					# assume second relationship is a new statement
					statements.append(statement)
					statement = Statement()

				statement.relate(r)
				continue

			if isinstance(r, Term):
				# Add terms to the current expression
				expression.add(r)
				continue

	if len(expression.terms) > 0:
		statement.add(expression)

	if statement.relation is None:
		# assume equality relationship
		statement.relate(Relation.EQUIVALENCE)

	if len(statement.expressions) == 1:
		# assign a variable
		statement.add(Expression([Term(Term.VARIABLE, Symbol("x"))]))

	statements.append(statement)
	return statements

def parse_word_problem(sentences):

	for sentence in sentences:
		tags = pos_tag(word_tokenize(sentence))
		print "Sentence: {0}".format(sentence)
		print "Tags:", tags

	return []

def get_statements(sentences):
	words = []
	for sentence in sentences:
		words.extend(word_tokenize(sentence))

	if len(list(set(Relation.TESTER) & set(words))) > 0:
		print "Assumption: Mathematics proposition(s)"
		return parse_proposition(sentences)
	else:
		print "Assumption: Word problem"
		return parse_word_problem(sentences)

# Solvers
def solve_problem(problem):
	tokenizer = load("tokenizers/punkt/english.pickle")
	sentences = tokenizer.tokenize(problem.strip())
	statements = get_statements(sentences)

	print "Problem input: {0}".format(problem)

	for s in statements:
		print "Statement: {0}".format(str(s))
		print "Solution: {0}".format(s.solve())

# Script
def argparser():
	desc = "Solves word problems."
	parser = ArgumentParser(description=desc)
	parser.add_argument("--input", type=FileType("r"), default="-",
						help="The question to solve")
	return parser

def main():
	args = argparser().parse_args()
	solve_problem(args.input.read())

if __name__ == "__main__":
	main()

