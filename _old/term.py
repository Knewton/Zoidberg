#!/usr/bin/env python
"""Zoidberg Term"""
class Term(object):
	VALUE="val"
	OPERATION="op"
	FUNCTION="func"

	def __init__(self, type, value):
		self.type = type
		self.value = value

	def __str__(self):
		return str(self.value)

