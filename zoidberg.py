#!/usr/bin/env python
from argparse import ArgumentParser, FileType
from sys import exit, stdout
from re import compile
from nltk.data import load
from nltk import word_tokenize

# Representations
class Expression(object):
	"""Representation of a mathematical expression"""
	CONSTANT="const"
	VARIABLE="var"
	OPERATION="op"
	FUNCTION="func"

	def __init__(self, type, value):
		self.type = type
		self.value = value

	def __str__(self):
		return "[{0}={1}]".format(self.type, self.value)

class Proposition(object):
	"""Representation of a mathematical proposition"""
	def __init__(self):
		self.expressions = []

	def add(self, exp):
		self.expressions.append(exp)

	def __str__(self):
		return "({0})".format("".join([str(e) for e in self.expressions]))

# Testers
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

# Interpreters
def to_number(s):
	return float(s) if '.' in s else int(s)

# Parsers
def get_expression(word):
	"""Parses a word into an expression.

	Args:
		word: The word to parse.

	Returns:
		The expression, or None
	"""
	exp = None

	if is_number(word):
		exp = Expression(Expression.CONSTANT, to_number(word))

	return exp

def get_proposition(sentence):
	"""Parses a sentence into an proposition.

	Args:
		sentence: The sentence to parse.

	Return:
		The equation detected in the sentence.
	"""
	prop = Proposition()

	for word in word_tokenize(sentence):
		exp = get_expression(word)
		if exp is not None:
			prop.add(exp)

	return prop

# Solvers
def solve_problem(problem):
	tokenizer = load("tokenizers/punkt/english.pickle")
	sentences = tokenizer.tokenize(problem.strip())
	propositions = [get_proposition(s) for s in sentences]

	print "\n".join([str(p) for p in propositions])

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

