#!/usr/bin/env python
"""Zoidberg conversions"""
from definitions import Operation, Relation

# Utility
def members(cls):
	return [a for a in dir(cls) if not callable(a) and not a.startswith("__")]

def convert(s, cls):
	for m in members(cls.Defs):
		if s in getattr(cls.Defs, m):
			return getattr(cls, m)
	raise ValueError

# Conversion operations
def to_number(s):
	if s.isalpha():
		raise NotImplementedError("Can't handle alpha numbers yet")
	else:
		return float(s) if '.' in s else int(s)

def to_operation(s):
	return convert(s, Operation)

def to_relation(s):
	return convert(s, Relation)
