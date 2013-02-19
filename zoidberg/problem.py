#!/usr/bin/env python
from nltk import word_tokenize, pos_tag, data
from brain import Brain
from inference import Inference
from query import Query

class Problem(object):
	def __init__(self, text, brain_path=None):
		# Problem text
		self.text = text

		# Problem brain
		self.brain = Brain(brain_path)

		# Digest
		self.sentences = None
		self.sentence_tags = None
		self.all_tags = None
		self.all_words = None
		self.longest_word = None

		# Engines
		self.inference = None
		self.question = None

	def digest(self):
		if self.sentences is not None:
			return

		# Digest the problem into sentences
		tokenizer = data.load("tokenizers/punkt/english.pickle")
		self.sentences = tokenizer.tokenize(self.text.strip())

		# Digest each sentence into words and part-of-speech tags
		if self.sentence_tags is None:
			sentence_tags = []
			all_tags = []
			all_words = []
			for s in self.sentences:
				all_words.append(s)
				tags = pos_tag(word_tokenize(s))
				sentence_tags.append(tags)
				for t in tags:
					l = len(t[0])
					if not self.longest_word or self.longest_word < l:
						self.longest_word = l
					all_tags.append(t[1])
			self.sentence_tags = sentence_tags
			self.all_tags = list(set(all_tags))
			self.all_words = list(set(all_words))

	def infer(self):
		if self.inference is not None:
			return

		self.digest()
		self.inference = Inference(self)

	def query(self):
		if self.question is not None:
			return

		self.infer()
		self.question = Query(self)

	def solve(self):
		self.query()
		self.brain.dump()

	def __str__(self):
		o = []

		o.append("# Zoidberg Solution")
		o.append("## The problem")
		o.append(self.text)

		o.append("## Digested problem")
		for s_tags in self.sentence_tags:
			words, tags = [], []
			for tag in s_tags:
				words.append("{: <{l}}".format(tag[0], l=self.longest_word))
				tags.append("{: <{l}}".format(tag[1], l=self.longest_word))
			o.append("\t".join(words))
			o.append("\t".join(tags))
			o.append("")

		if self.inference is not None:
			o.append(str(self.inference))
			o.append("")

		if self.question is not None:
			o.append(str(self.question))
			o.append("")

		return "\n".join(o)
