#!/usr/bin/env python
"""Zoidberg Standard Interpreter

Adds interpretation to a provided Problem object.
"""
import inferences as infer

class Interpretation(object):
	def __init__(self, problem):
		# Thought log
		self.thoughts = []

		# Current state

		# Output

		# Begin the interpretation
		for sentence_tags in problem.sentence_tags:
			for t in sentence_tags:
				self._interpret(*t)

	def _think(self, thought, *args):
		self.thoughts.append(thought.format(*args))

	def _interpret(self, word, tag):
		if word.isalpha():
			self._think("{0} is alpha", word)
		else:
			if infer.is_number(word):
				self._think("{0} is a number", word)

	def __str__(self):
		return "\n".join(self.thoughts)
