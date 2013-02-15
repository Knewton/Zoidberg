#!/usr/bin/env python
from nltk import word_tokenize, pos_tag, data

class Problem(object):
	def __init__(self, text):
		# Problem text
		self.text = text

		# Digest
		self.sentences = None
		self.sentence_tags = None
		self.all_tags = None
		self.all_words = None
		self.longest_word = None
		self.digest()

	def digest(self):
		# Digest the problem into sentences
		if self.sentences is None:
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

	def solve(self):
		pass

	def __str__(self):
		o = []

		o.append("# Zoidberg Solution")
		o.append("## The problem")
		o.append(self.text)

		o.append("## Parsed problem")
		for s_tags in self.sentence_tags:
			words, tags = [], []
			for tag in s_tags:
				words.append("{: <{l}}".format(tag[0], l=self.longest_word))
				tags.append("{: <{l}}".format(tag[1], l=self.longest_word))
			o.append("\t".join(words))
			o.append("\t".join(tags))
			o.append("")

		return "\n".join(o)
