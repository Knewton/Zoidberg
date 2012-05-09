#!/usr/bin/env python
"""Zoidberg Expression"""
from term import Term

class Expression(object):
	def __init__(self):
		self.terms = []

	def operations(self):
		return list(set([o.value for o in self.terms
									if o.type is Term.OPERATION]))

	def __str__(self):
		return "{Expression}"
