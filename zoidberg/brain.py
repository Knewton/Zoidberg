#!/usr/bin/env python
from utilities import get_json, set_json
import sys

DEFAULT_PATH = "~/.zoidberg.brain.json"
DEFAULT_BRAIN = {
	"operator_verbs": {},
	"subordinates": {}
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

def _input(data, prompt):
	i = 0
	for k in data:
		i += 1
		print "	{0}. {1}".format(i, k[1])

	sys.stdin = open('/dev/tty')
	r = int(raw_input(prompt))

	if r < 0 or r > len(data):
		return _input(data, prompt)
	return data[r - 1][0]

def input_operator_type(x):
	print "What operation does the verb '{0}' indicate?".format(x)
	return _input(OPERATORS, "'{0}' indicates: ".format(x))

def input_subordinate_type(x):
	print "What subordinate does '{0}' indicate?".format(x)
	return _input(SUBORDINATES, "'{0}' indicates: ".format(x))

class Brain(object):
	def __init__(self, path=None):
		if path is None:
			path = DEFAULT_PATH

		self.path = path
		self.raw = get_json(self.path)
		if self.raw is None:
			self.raw = DEFAULT_BRAIN

	def _proc(self, key, val, fn):
		if not key in self.raw:
			self.raw[key] = {}
		if not val in self.raw[key]:
			self.raw[key][val] = fn(val)
		return self.raw[key][val]

	def subordinate(self, sub):
		return self._proc("subordinates", sub, input_subordinate_type)

	def operator(self, verb):
		return self._proc("operator_verbs", verb, input_operator_type)

	def dump(self):
		set_json(self.path, self.raw)
