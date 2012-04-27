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

class AnswerType:
	# Answer is likely a number
	NUMERIC="num"

class Relation:
	EQUIVALENCE="="
	ALL=["="]
	TESTER=["="]

# Values
uid = 0 # Variable manufacturing

# Representations
class QuestionInterpretation(object):
	def __init__(self, type, var, unit=None):
		self.type = type
		self.var = Symbol(var)
		self.unit = unit

	def __str__(self):
		out = []
		# Answer type formatting
		if self.type == AnswerType.NUMERIC:
			out.append("Number of")

		out.append(str(self.var))

		if self.unit is not None:
			out.append(self.unit)

		return "Question Interpretation: {0}.".format(" ".join(out))

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

def new_var():
	global uid
	var = "zoid_{0}".format(uid)
	uid += 1
	return Symbol(var)

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
		statement.add(Expression([Term(Term.VARIABLE, new_var())]))

	statements.append(statement)
	return statements

def estimate_answer_type(word):
	# Indicates a numeric answer type
	if word in ["many"]:
		return AnswerType.NUMERIC
	raise Exception("Did not estimate answer type")

def total_equivalence_statement(unit_values):
	total_exp = Expression()
	summative_exp = Expression()

	statement = Statement()
	statement.relate(Relation.EQUIVALENCE)
	statement.add(total_exp)
	statement.add(summative_exp)

	summative_terms = []
	# Solving for a total is an explicit equivalence relation
	for k in unit_values.keys():
		val = unit_values[k]
		term = Term(Term.VARIABLE, val)

		if k == "__total__":
			total_exp.add(term)
		else:
			summative_terms.append(term)
			summative_terms.append(Term(Term.OPERATION, Operation.ADDITION))

	# Remove the hanging addition operation
	summative_terms.pop()
	summative_exp.terms.extend(summative_terms)

	return statement

def interpret_question(question):
	print "Interpreting question..."

	# Assumption flags
	next_adjective_ordinal = False
	next_noun_target_variable = False
	next_adjective_context = False

	# Interpretation
	answer_type = None
	solution_var = None
	solution_unit = None

	question_words = word_tokenize(question)
	question_tags = pos_tag(question_words)

	for t in question_tags:
		word, tag = t
		# WRB is a Wh-Adverb (who, what, why) and a good indicator for the
		# question start
		if tag == "WRB":
			print "  '{0}' colors next adjective as ordinal".format(word)
			next_adjective_ordinal = True

		# An Adjective or ordinal; likely ordinal if an adverb preceeds it.
		# Could also be a good ordinal candidate when followed by a verb
		# If colored for context, may revamp target variable
		if tag == "JJ":
			if next_adjective_ordinal and answer_type is None:
				print "  '{0}' likely used as an ordinal".format(word)
				next_adjective_ordinal = False
				answer_type = estimate_answer_type(word)
				# Assume the next noun is the variable we care about
				next_noun_target_variable = True

			if next_adjective_context:
				print "  New assumption: '{0}' likely variable".format(word)
				print "  '{0}' likely unit for variable".format(solution_var)
				solution_unit = solution_var
				solution_var = word

		# Common plural noun; good candidate for variable to identify
		if tag == "NNS":
			if next_noun_target_variable and solution_var is None:
				print "  '{0}' likely the variable to solve for".format(word)
				solution_var = word
				next_noun_target_variable = False

		# Present tense verb; candidate for criteria filtering
		if tag == "VBP":
			if solution_var is not None:
				print "  '{0}' colors next adjective as context".format(word)
				next_adjective_context = True

	if not answer_type or not solution_var:
		raise Exception("Could not interperet question")

	return QuestionInterpretation(answer_type, solution_var, solution_unit)

def conveys_ownership(word):
	return word in ["has"]

def conveys_equality(word):
	return word in ["are"]

def conveys_symbolic_value(word):
	# "the rest"
	return word in ["rest"]

def extract_statements(interp, sentences):
	# Assumptions
	group_into_context = False
	pending_equality = False
	last_pending_action = None

	# Interpretation
	# Context around variable ownership
	context_groups = []
	# Groupings by context for ownership
	groupings = {}
	# A listing of values for a unit by it's variable type
	unit_values = {}
	last_constant = None
	last_variable = None
	# Current important bits for tracking and implicit reference
	current_unit = None
	current_context = None

	def define_unit(unit, type, val):
		if not unit in unit_values.keys():
			unit_values[unit] = {}
		print "  {0} {1} = {2}".format(type, unit, val)
		unit_values[unit][type] = val
		if current_context is not None:
			groupings[current_context].append(["unit_values", unit, type])

	for sentence in sentences:
		print "Extracting statements from: {0}".format(sentence)

		words = word_tokenize(sentence)
		tags = pos_tag(words)
		# Debugging
		#print tags
		for t in tags:
			word, tag = t

			# Proper noun; likely used for contextual grouping
			if tag == "NNP":
				print "  '{0}' likely context for grouping".format(word)
				if word not in context_groups:
					context_groups.append(word)
					groupings[word] = []
				# assign current context
				print "  '{0}' is the new context".format(word)
				current_context = word

			# Present tense verbs
			if tag in ["VBZ", "VBP"]:
				if conveys_ownership(word) and current_context is not None:
					print "  '{0}' conveys ownership for context".format(word)
					group_into_context = True
				if conveys_equality(word):
					print "  '{0}' conveys equality".format(word)
					if last_variable is None and last_constant is not None:
						print "  Equality assignment pending"
						pending_equality = True

			# Adjective or numerical ordinal; good candidate for variable id
			if tag == "JJ":
				if pending_equality and current_unit and last_constant:
					if word == interp.var:
						print "  '{0}' is the solution var".format(word)
						if isinstance(last_constant, Symbol):
							print "  Last constant is a symbol; looks good"
						else:
							print "  Solution var is not a symbol; looks bad"
					define_unit(current_unit, word, last_constant)
					last_constant = None
					pending_equality = False
					last_pending_action = "equality"

			# Singular or mass noun, may indicate a symbolic value
			if tag == "NN":
				if not last_constant and conveys_symbolic_value(word):
					print "  '{0}' conveys a symbolic variable".format(word)
					last_constant = new_var()

			# Conjunction; continue defining in the current context and unit
			if tag == "CC":
				print "  Conjunction found, next variable likely in same unit"
				if last_pending_action == "equality":
					print "  Conjunction reactivates pending equality"
					pending_equality = True

			# Numeric/cardinal
			if tag == "CD":
				print "  Setting '{0}' as last_constant".format(word)
				last_constant = to_number(word)

			# Common plural noun; good candidate for variable identification
			if tag == "NNS":
				if word == interp.var:
					print "  '{0}' is the solution variable".format(word)
				if word == interp.unit:
					current_unit = word
					print "  '{0}' is now the current unit".format(word)
					print "  '{0}' is the solution unit".format(word)
					if last_constant is not None:
						if last_variable is None:
							define_unit(word, "__total__", last_constant)
						last_constant = None
						last_pending_action = "implicit_constant"

	statements = []
	if len(context_groups) == 1:
		context_containing_answer = context_groups[0]
		print "Only one context; statement should contain answer"

	print "Forming statements..."
	for group in context_groups:
		print "Processing context group '{0}'".format(group)
		solve_units = []

		for blob in groupings[group]:
			if blob[0] == "unit_values":
				t, unit, var = blob
				val = unit_values[unit][var]
				print "  owns {0} {1} {2}".format(val, var, unit)
				if isinstance(val, Symbol):
					if var == interp.var:
						print "  {0} answers question!".format(var)
					solve_units.append(unit)
					print "  Symbol '{0}' needs solving".format(val)

		if len(solve_units) > 0:
			for unit in solve_units:
				if "__total__" in unit_values[unit].keys():
					print "Creating equality for unit '{0}'".format(unit)
					statement = total_equivalence_statement(unit_values[unit])

				if unit == interp.unit and group == context_containing_answer:
					print "Unit answers question!"
					statements.append(statement)
	return statements

def parse_word_problem(sentences):
	# Break the word problem down into the question being asked and the
	# details which likely contain the info needed to answer the question.
	# This info will be condensed into mathematical statements.
	questions, details = [], []
	question = None

	# Attempt to find the question to answer
	for s in sentences:
		if "?" in s:
			questions.append(s)
		else:
			details.append(s)
	if len(questions) != 1:
		# Handle only single questions right now. Multipart is probably harder.
		raise Exception("Could not detect the question")

	question = questions[0]
	print "Assumed question to answer: {0}".format(question)
	interpretation = interpret_question(question)
	print str(interpretation)

	print "Gathering data..."
	return extract_statements(interpretation, details)

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

	print "Problem input: {0}".format(problem)

	for s in get_statements(sentences):
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

