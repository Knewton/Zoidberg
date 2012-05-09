#!/usr/bin/env python
"""Zoidberg Inferences

A collection of function to make inferences on how a word should be used.
"""
import converter as convert

# Decorator for capturing conversion failures
def test_conversion(fn):
	def t(*args):
		try:
			fn(*args)
			return True
		except ValueError:
			return False
	return t

# Conversion testing

@test_conversion
def is_number(s):
	float(s)

@test_conversion
def is_operation(s):
	convert.to_operation(s)

