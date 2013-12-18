#!/usr/bin/env python
from os.path import isfile, realpath, expanduser
from utilities import get_json, set_json
import sys
import json

DEFAULT_PATH = "~/.zoidberg.brain.json"
DEFAULT_BRAIN = {
	"operator_verbs": {},
	"subordinates": {},
	"comparison_adj": {},
	"answer_syntax": {},
	"plurality": {},
	"gender": {},
	"retagged": {},
	"determiners": {},
	"inclusive": {},
	"relative": {},
	"gerunds": {},
	"numbers": {},
	"variables": {}
}

# Various mathematical operators we know of
OPERATORS = [
	("eq", "Equals"),
	("ad", "Addition"),
	("su", "Subtraction"),
	("mu", "Multiplication"),
	("di", "Division"),
	("re", "Requires (the total we need to answer)"),
	("co", "Convert (change one unit into another)")
]

# Various types of supported subordinace
SUBORDINATES = [
	("time_starting", "Time: Beginning"),
	("time_ending", "Time: Ending"),
	("place_noun", "Place (pond, mall, home, work)"),
	("context_grouping", "Context Grouping (Group by owners of units [total items owned by all])"),
	("unit_grouping", "Unit Grouping (Group by units [total golfballs])")
]

RELATIVE = [
	("noise", "This indicates no relative numerical relationship"),
	("rel_more", "This indicates a 'more than' relationship."),
	("rel_less", "This indicates a 'less than' relationship.")
]

INCLUSIVE = [
	("inclusive", "Yes, it is inclusive (her family)"),
	("exclusive", "No, it is exclusive (his friends, her parents)")
]

DETERMINERS = [
	("noise", "This has no numeric connotations. (The)"),
	("constant", "This has a constant numeric connotation (a/an)"),
	("variable", "This has a variable connotation (some)")
]

GERUNDS = [
	("noise", "This has no numeric connotations. (walking)"),
	("solution_zero", "Connotes the ending value is zero (remaining)"),
	("acting", "Is some action being performed (dancing, swimming)")
]

COMPARISONS = [
	("gt", "Greater than"),
	("lt", "Less than"),
	("gr", "Greatest"),
	("le", "Least"),
	("av", "Average")
]

ANSWERS = [
	("expression", "Answer is the solution to an expression (4 cars)"),
	("unit", "Answer is the unit of the solution to an expression (cars)"),
	("context", "Answer is the owner of the solution to an expression (Joe)")
]

PLURALITY = [
	("singular", "Refers to a single (balloon, she)"),
	("plural", "Refers to a plural (balloons, they)"),
	("regular", "Refers to a regular plural (fish, sheep)")
]

GENDERS = [
	("masculine", "Refers to a male gender"),
	("feminine", "Refers to a female gender"),
	("neutral", "Refers to a non-gendered entity"),
	("mixed", "Refers to a mixture of/ambiguous genders (a group of )"),
	("ambiguous", "Refers to a man or woman but is not clear enough to know")
]

RETAGS = [
	("noise", "This is not relevant to the question and can be ignored"),
	("operator_verbs", "This indicates a mathematical operation"),
	("subordinates", "This indicates a point in time"),
	("comparison_adj", "This indicates a comparison between things"),
	("answer_syntax", "This frames the answer to the question"),
	("numbers", "This is a cardinal number"),
	("pre_ind_plu", "This is present indicitive plural (someone ->is<-, they ->are<-)"),

	("noun", "Singular or mass noun"),
	("noun_p", "Plural noun"),

	("prop_noun", "Singular proper noun"),
	("prop_noun_p", "Plural proper noun"),

	("pers_pro", "Personal pronoun"),
	("pos_pro", "Possessive pronoun"),

	("wh_pro", "Wh-pronoun"),
	("pos_wh_pro", "Possessive Wh-pronoun"),
]

INPUT_STR = "What {0} does {1}'{2}' indicate in the sentence: '{3}'"

def get_input(data, prompt, x, ref, brain, force_retag=False):
	msg = "\t{0}. {1}"
	sys.stdin = open('/dev/tty')

	def retag():
		if not force_retag:
			print "Okay, how should '{0}' be treated?".format(x)
		i = 0
		for k in RETAGS:
			i += 1
			print msg.format(i, k[1])
		e = int(raw_input(prompt))
		if e < 0 or e > len(RETAGS):
			return retag()
		item = RETAGS[e - 1][0]
		brain.add("retagged", x, item)

		# This sets us up to call any of the processors again for the
		# retagged value
		if item == "subordinates":
			brain.subordinate((x, "UNKNOWN"), ref)
		elif item == "operator_verbs":
			brain.operator(x, ref)
		elif item == "comparison_adj":
			brain.comparison(x, ref)
		elif item == "answer_syntax":
			brain.answer_syntax(x, ref)
		elif item == "noun":
			brain.noun_like(x, "NN", ref)
		elif item == "noun_p":
			brain.noun_like(x, "NNS", ref)
		elif item == "prop_noun":
			brain.noun_like(x, "NNP", ref)
		elif item == "prop_noun_p":
			brain.noun_like(x, "NNPS", ref)
		elif item == "pers_pro":
			brain.noun_like(x, "PRP", ref)
		elif item == "pos_pro":
			brain.noun_like(x, "PRP$", ref)
		elif item == "wh_pro":
			brain.noun_like(x, "WP", ref)
		elif item == "pos_wh_pro":
			brain.noun_like(x, "WP$", ref)
		elif item == "numbers":
			brain.number(x, ref)
		elif item == "variable":
			brain.variable(x, ref)
		elif item == "noise":
			brain.add("determiners", x, "noise")
			# A false in the indicator means it's noise and can be ignored
			return False

		# None in any of the values in an indicator that it's been retagged
		# This is for the original add
		return None

	if force_retag:
		return retag()

	i = 0
	print "\t0. This word has been misidentified."
	for k in data:
		i += 1
		print msg.format(i, k[1])

	r = int(raw_input(prompt))

	if r == 0:
		return retag()

	if r < 0 or r > len(data):
		return get_input(data, prompt, x, brain)
	return data[r - 1][0]

def input_operator_type(x, ref, brain):
	print INPUT_STR.format("operation", "the verb ", x, ref)
	return get_input(OPERATORS, "'{0}' indicates: ".format(x), x, ref, brain)

def input_unknown(pack, ref, brain):
	x, tag, subtype = pack
	print INPUT_STR.format("concept", tag + " ", x, ref)
	return get_input([], "'{0}' is: ".format(x), x, ref, brain, True)

def input_subordinate_type(x, ref, brain):
	print INPUT_STR.format("subordinate", "", x, ref)
	return get_input(SUBORDINATES, "'{0}' indicates: ".format(x), x, ref,
			brain)

def input_comparison_type(x, ref, brain):
	print INPUT_STR.format("comparison", "", x, ref)
	return get_input(COMPARISONS, "'{0}' indicates: ".format(x), x, ref, brain)

def input_answer_syntax(x, ref, brain):
	print INPUT_STR.format("question", "", x, ref)
	return get_input(ANSWERS, "'{0}' indicates: ".format(x), x, ref, brain)

def input_plurality(p, ref, brain):
	x, tag = p

	pos = "improper noun"

	if tag in ["PRP", "PRP$", "WP", "WP$"]:
		pos = "pronoun"

	if tag in ["NNP", "NNPS"]:
		pos = "proper noun"
		x = x.capitalize()

	print INPUT_STR.format("plurality", "the {} ".format(pos), x, ref)
	return get_input(PLURALITY, "'{0}' indicates: ".format(x), x, ref, brain)

def input_gender(p, ref, brain):
	x, tag = p

	if tag in ["NNP", "NNPS"]:
		x = x.capitalize()

	print INPUT_STR.format("gender", "", x, ref)
	return get_input(GENDERS, "'{0}' indicates: ".format(x), x, ref, brain)

def input_determiner(x, ref, brain):
	print INPUT_STR.format("type", "the determiner ", x, ref)
	return get_input(DETERMINERS, "'{0}' indicates: ".format(x), x, ref, brain)

def input_gerund(x, ref, brain):
	print INPUT_STR.format("type", "the gerund ", x, ref)
	return get_input(GERUNDS, "'{0}' indicates: ".format(x), x, ref, brain)

def input_relative(x, ref, brain):
	print INPUT_STR.format("relative relationship", "the adjective ", x, ref)
	return get_input(RELATIVE, "'{0}' indicates: ".format(x), x, ref, brain)

def input_inclusive(x, ref, brain):
	print "Is the group '{0}' inclusive of {1}?".format(x, ref)
	return get_input(INCLUSIVE, "'{0}' is: ".format(x), x, ref, brain)

def input_variable(x, ref, brain):
	print INPUT_STR.format("variable quantity", "", x, ref)
	prompt = "Please input the fixed numerical relationship of '{0}' as a decimal value (or 'd' for 'dyanamic'): ".format(x)
	sys.stdin = open('/dev/tty')
	r = raw_input(prompt)
	try:
		if r == "":
			r = x
		r = float(r) if "." in r else int(r)
		return r
	except ValueError:
		if r == "d":
			return "dynamic_variable"
		else:
			return input_variable(x, ref, brain)

def input_number(x, ref, brain):
	print INPUT_STR.format("numeric quantity", "", x, ref)
	prompt = "Please input the actual numerical value of '{0}': ".format(x)
	sys.stdin = open('/dev/tty')
	r = raw_input(prompt)
	try:
		if r == "":
			r = x
		r = float(r) if "." in r else int(r)
		return r
	except ValueError:
		return input_number(x, ref, brain)

class Brain(object):
	def __init__(self, path=None):
		if path is None:
			path = DEFAULT_PATH

		self.path = realpath(expanduser(path))
		self.raw = None
		if isfile(self.path):
			self.raw = get_json(self.path)
		if self.raw is None:
			self.raw = DEFAULT_BRAIN

	def add(self, key, val, value):
		key = str(key)
		val = str(val)
		o = None
		if value is not None:
			value = str(value)

		if not key in self.raw:
			self.raw[key] = {}
		if not val in self.raw[key]:
			self.raw[key][val] = value
#			print json.dumps(self.raw, sort_keys=True, indent=4)
		elif self.raw[key] == None:
			# Retagged
			return self.raw[self.raw["retagged"][val]][val]
		return self.raw[key][val]

	def retag(self, val, tag):
		if val in self.raw["retagged"]:
			item = self.raw["retagged"][val]
			if item == "subordinates":
				tag = "SUB"
			elif item == "operator_verbs":
				tag = "VBX"
			elif item == "comparison_adj":
				tag = "COMP"
			elif item == "answer_syntax":
				tag = "ANSYX"
			elif item == "noun":
				tag = "NN"
			elif item == "noun_p":
				tag = "NNS"
			elif item == "prop_noun":
				tag = "NNP"
			elif item == "prop_noun_p":
				tag = "NNPS"
			elif item == "pers_pro":
				tag = "PRP"
			elif item == "pos_pro":
				tag = "PRP$"
			elif item == "wh_pro":
				tag = "WP"
			elif item == "pos_wh_pro":
				tag = "WP$"
			elif item == "noise":
				tag = "DT"
			elif item == "numbers":
				tag = "CD"
				val = str(self.raw["numbers"][val])
			elif item == "pre_ind_plu":
				tag = "PIP"
			else:
				print item
				tag = "!!!"
		return (val, tag)

	def proc(self, key, val, fn, ref, exp=None):
		value = None
		if exp is None:
			exp = val
		if not key in self.raw or not exp in self.raw[key]:
			value = fn(val, ref, self)
		return self.add(key, exp, value)

	def subordinate(self, p, ref):
		sub, tag = p
		subtype = self.proc("subordinates", sub, input_subordinate_type, ref)
		if subtype == "place_noun":
			self.noun_like(sub, tag, ref)
		return subtype

	def operator(self, verb, ref):
		return self.proc("operator_verbs", verb, input_operator_type, ref)

	def comparison(self, comp, ref):
		return self.proc("comparison_adj", comp, input_comparison_type, ref)

	def answer_syntax(self, query, ref):
		return self.proc("answer_syntax", query, input_answer_syntax, ref)

	def noun_like(self, n, tag, ref):
		if tag in ["NNP", "NNPS"]:
			n = n.capitalize()

		plurality = self.proc("plurality", (n, tag), input_plurality, ref, n)
		if plurality is None:
			gender = None
		else:
			gender = self.proc("gender", (n, tag), input_gender, ref, n)
		return (plurality, gender)

	def determiner(self, n, ref):
		return self.proc("determiners", n, input_determiner, ref)

	def gerund(self, n, ref):
		return self.proc("gerunds", n, input_gerund, ref)

	def inclusive(self, n, ref):
		return self.proc("inclusive", n, input_inclusive, ref)

	def is_inclusive(self, n):
		if n in self.raw["inclusive"]:
			return self.raw["inclusive"][n] == "inclusive"
		return False

	def relative(self, n, ref):
		return self.proc("relative", n, input_relative, ref)

	def unknown(self, n, tag, subtype, ref):
		return self.proc("unknown", (n, tag, subtype), input_unknown, ref)

	def number(self, n, ref):
		return self.proc("numbers", n, input_number, ref)

	def variable(self, n, ref):
		return self.proc("variables", n, input_variable, ref)

	def dump(self):
		set_json(self.path, self.raw)

