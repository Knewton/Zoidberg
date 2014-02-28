#!/usr/bin/env python
from utilities import output_tuples, uniq
from nltk import word_tokenize, pos_tag, data
from brain import Brain
from inference import Inference
from query import Query
from solution import Solution

class Problem(object):
	def __init__(self, text, brain_path=None, file_name=None):

		self.file_name = file_name

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
		self.involves_acting = False
		self.units_acting_as_context = {}
		self.context_subordinates = {}
		self.context_actions = {}
		self.descriptive_units = []
		self.refined_units = {}
		self.unit_subtypes = {}
		self.context_subtypes = {}
		self.units = []
		self.running_units = []

		self.exestential = False
		self.adaptive_context = {}
		self.last_contexts = {
			"plurality": {
				"singular": None,
				"plural": None,
				"self": None,
				"regular": None
			},
			"gender": {
				"masculine": None,
				"feminine": None,
				"neutral": None,
				"mixed": None,
				"self": None,
				"ambiguous": None
			},
			"last": None
		}
		self.subordinate_adaptive_contexts = []
		self.previous_contexts = {
			"plurality": {
				"singular": None,
				"plural": None,
				"self": None,
				"regular": None
			},
			"gender": {
				"masculine": None,
				"feminine": None,
				"neutral": None,
				"mixed": None,
				"self": None,
				"ambiguous": None
			},
			"last": None
		}
		self.all_targets = {
			"plurality": {
				"singular": {},
				"plural": {},
				"self": {},
				"regular": {}
			},
			"gender": {
				"masculine": {},
				"feminine": {},
				"neutral": {},
				"mixed": {},
				"self": {},
				"ambiguous": {}
			},
			"last": None
		}
		self.contexts = []
		self.all_contexts = {
			"plurality": {
				"singular": {},
				"plural": {},
				"self": {},
				"regular": {}
			},
			"gender": {
				"self": {},
				"masculine": {},
				"feminine": {},
				"neutral": {},
				"mixed": {},
				"ambiguous": {}
			},
			"last": None
		}

		# Engines
		self.inference = None
		self.question = None
		self.solution = None

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
			self.all_tags = uniq(all_tags)
			self.all_words = uniq(all_words)

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
		if self.solution is not None:
			return

		self.query()
		self.solution = Solution(self)

		# Maybe move this into a different mode so you can see everything but
		self.solution.compute_correct()
		self.brain.dump()

	def __str__(self):
		o = []

		o.append("# Zoidberg Solution")

		if self.file_name:
			o.append("File: {0}".format(self.file_name))

		o.append("\n## The problem")
		o.append("    " + "\n    ".join(self.text.split("\n")))

		o.append("## Digested problem")
		output_tuples(self.sentence_tags, o, self.longest_word, self.brain)

		if self.inference is not None:
			o.append(str(self.inference))

		if self.question is not None:
			o.append(str(self.question))

		if self.solution is not None:
			o.append(str(self.solution))

		return "\n".join(o)
