#!/usr/bin/env python
"""Zoidberg Problem

A representation of a word problem, it's parsed language components,
mathematical interpretation, and ultimate solution.

All problems are solved using a three step process.

1. Use NLP to add part-of-speech tags to words in the problem.
2. Use the tags to infer word meaning and create a model of the problem.
3. Use a symbolic math engine to solve statements created from the model.

Each of these steps can be run independently from this Problem wrapper.
	problem.parse() - Runs the NLP tagger
	problem.interpret() - Processes the tags to create a model of the problem.
	problem.solve() - Converts the model into statements and solves them.

You can print the problem as a string to view a trace of whatever action has
been done on the problem. For instance the following code would parse the
problem and interpert it, then display the parsing output and problem model.
	problem.interpert()
	print str(problem)

Enabling debugging for a problem prints additional information which is helpful
for spotting interpretation problems so the program can be enhanced to handle
them.
"""
from nltk.data import load
from nltk import word_tokenize, pos_tag
from interpreter import Interpretation
from solver import Solution

class Problem(object):
	def __init__(self, text, debug=False):
		# Configuration
		self.debug = debug

		# Problem text
		self.text = text
		self.sentences = None
		self.sentence_tags = None
		self.all_tags = None

		# Interpretation
		self.interpretation = None

		# Problem interpretation
		self.solution = None

	def parse(self):
		# Break the problem into sentences
		if self.sentences is None:
			tokenizer = load("tokenizers/punkt/english.pickle")
			self.sentences = tokenizer.tokenize(self.text.strip())

		# Break each sentence into words and identify with part-of-speech tags
		if self.sentence_tags is None:
			sentence_tags = []
			all_tags = []
			for s in self.sentences:
				tags = pos_tag(word_tokenize(s))
				sentence_tags.append(tags)
				for t in tags:
					all_tags.append(t[1])
			self.sentence_tags = sentence_tags
			self.all_tags = list(set(all_tags))

		return self.sentence_tags

	def interpret(self):
		if self.interpretation is None:
			self.parse()
			self.interpretation = Interpretation(self)

		return self.interpretation

	def solve(self):
		if self.solution is None:
			self.interpret()
			self.solution = Solution(self)

		return self.solution

	def get_answer(self):
		self.solve()
		return self.solution.answer

	def __str__(self):
		"""Output the problem details in asciidoc"""
		out = []

		# Helpers
		def title(t, tier="=="):
			out.append("{0} {1}".format(tier, t))

		def block(t):
			out.append("****\n{0}\n****\n".format(t))

		# Create output
		title("Problem")
		out.append(self.text)

		if self.interpretation is not None:
			title("Interpretation")
			out.append(str(self.interpretation))

		if self.solution is not None:
			title("Solution")
			out.append(str(self.solution))

			title("Answer")
			block(self.solution.answer)

		if self.debug:
			title("Debugging")
			if self.sentence_tags is not None:
				# Display all the sentence tags
				title("Sentences", "===")
				for tags in self.sentence_tags:
					block(str(tags))

				# Define what each tag means
				title("Tags", "===")
				tagdict = load('help/tagsets/upenn_tagset.pickle')
				for t in self.all_tags:
					if not t in tagdict:
						d = ("?", "No examples")
					else:
						d = tagdict[t]
					block("*Tag '{0}'*: {1}\n\n{2}".format(t, d[0], d[1]))

		return "\n".join(out) + "\n"

