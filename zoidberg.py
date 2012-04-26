#!/usr/bin/env python
from argparse import ArgumentParser, FileType
from sys import exit, stdout
from re import compile
from nltk.data import load
from nltk import word_tokenize

# Enums
class Operation:
	ADDITION="+"
	SUBTRACTION="-"
	MULTIPLICATION="*"
	DIVISION="/"
	ALL=["+", "-", "*", "/"]

class Relation:
	EQUIVALENCE="="
	ALL=["="]

# Representations
class Term(object):
	CONSTANT="const"
	VARIABLE="var"
	OPERATION="op"
	FUNCTION="func"

	def __init__(self, type, value):
		self.type = type
		self.value = value

	def __str__(self):
		return "[{0}:{1}]".format(self.type, self.value)

class Expression(object):
	def __init__(self, terms=[]):
		self.terms = terms

	def add(self, term):
		self.terms.append(term)

	def __str__(self):
		return "({0})".format("".join([str(t) for t in self.terms]))

class Statement(object):
	def __init__(self):
		self.expressions = []
		self.relation = None

	def add(self, exp):
		self.expressions.append(exp)

	def relate(self, relation):
		self.relation = relation

	def __str__(self):
		e = self.expressions
		if len(e) < 2:
			return "Malformed statement"
		else:
			return "{0}{{{1}}}{2}".format(e[0], self.relation, e[1])

# Testers
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def is_operation(s):
	return s in Operation.ALL

def is_relation(s):
	return s in Relation.ALL

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
	if s == "/":
		return Operation.DIVISION

def to_relation(s):
	if s == "=":
		return Relation.EQUIVALENCE

# Parsers
def parse_word(word):
	if is_number(word):
		return Term(Term.CONSTANT, to_number(word))

	if is_operation(word):
		return Term(Term.OPERATION, to_operation(word))

	if is_relation(word):
		return Relation.EQUIVALENCE

	return None

def get_statements(sentences):
	statements = []

	for sentence in sentences:
		statement = Statement()
		expression = Expression()

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

	if statement.relation is None:
		# assume equality relationship
		statement.relate(Relation.EQUIVALENCE)
		statement.add(expression)

	if len(statement.expressions) == 1:
		# assign a variable
		statement.add(Expression([Term(Term.VARIABLE, "x")]))

	statements.append(statement)
	return statements

# Solvers
def solve_problem(problem):
	tokenizer = load("tokenizers/punkt/english.pickle")
	sentences = tokenizer.tokenize(problem.strip())
	statements = get_statements(sentences)

	for s in statements:
		print str(s)

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

