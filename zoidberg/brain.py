#!/usr/bin/env python
from utilities import get_json, set_json
import sys

DEFAULT_PATH = "~/.zoidberg.brain.json"
DEFAULT_BRAIN = {
	"operator_verbs": {},
	"subordinates": {},
	"comparison_adj": {}
}

# Various mathematical operators we know of
OPERATORS = [
	("eq", "Equals"),
	("ad", "Addition"),
	("su", "Subtraction"),
	("mu", "Multiplication"),
	("di", "Division")
]

# Various types of supported subordinace
SUBORDINATES = [
	("time_starting", "Time: Beginning"),
	("time_ending", "Time: Ending")
]

COMPARISONS = [
	("gt", "Greater than"),
	("lt", "Less than"),
	("gr", "Greatest"),
	("le", "Least"),
	("av", "Average")
]

INPUT_STR = "What {0} does {1}'{2}' indicate in the sentence: '{3}'"

def get_input(data, prompt):
	i = 0
	for k in data:
		i += 1
		print "	{0}. {1}".format(i, k[1])

	sys.stdin = open('/dev/tty')
	r = int(raw_input(prompt))

	if r < 0 or r > len(data):
		return get_input(data, prompt)
	return data[r - 1][0]

def input_operator_type(x, ref):
	print INPUT_STR.format("operation", "the verb ", x, ref)
	return get_input(OPERATORS, "'{0}' indicates: ".format(x))

def input_subordinate_type(x, ref):
	print INPUT_STR.format("subordinate", "", x, ref)
	return get_input(SUBORDINATES, "'{0}' indicates: ".format(x))

def input_comparison_type(x, ref):
	print INPUT_STR.format("comparison", "", x, ref)
	return get_input(COMPARISONS, "'{0}' indicates: ".format(x))

class Brain(object):
	def __init__(self, path=None):
		if path is None:
			path = DEFAULT_PATH

		self.path = path
		self.raw = get_json(self.path)
		if self.raw is None:
			self.raw = DEFAULT_BRAIN

	def proc(self, key, val, fn, ref):
		if not key in self.raw:
			self.raw[key] = {}
		if not val in self.raw[key]:
			self.raw[key][val] = fn(val, ref)
		return self.raw[key][val]

	def subordinate(self, sub, ref):
		return self.proc("subordinates", sub, input_subordinate_type, ref)

	def operator(self, verb, ref):
		return self.proc("operator_verbs", verb, input_operator_type, ref)

	def comparison(self, comp, ref):
		return self.proc("comparison_adj", verb, input_comparison_type, ref)

	def dump(self):
		set_json(self.path, self.raw)

