#!/usr/bin/env python
"""Zoidberg Inferences

A collection of function to make inferences on how a word should be used.
"""
def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

