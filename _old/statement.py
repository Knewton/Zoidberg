#!/usr/bin/env python
"""Zoidberg statement"""

class Statement(object):
	def __init__(self):
		self.relation = None
		self.expressions = []

	def __str__(self):
		return "{Expression}"
