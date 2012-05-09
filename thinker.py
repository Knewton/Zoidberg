#!/usr/bin/env python
class Thinker(object):
	def __init__(self):
		# Thought log
		self.thoughts = []

	def _assume(self, assumption, *args):
		self._think("Assuming {0}".format(assumption), *args)

	def _think(self, thought, *args):
		self.thoughts.append(thought.format(*args))

	def __str__(self):
		return "\n".join(self.thoughts) + "\n"
