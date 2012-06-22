#!/usr/bin/env python
def quirk_fix(tag, word):
	thought = None
	if word == "ate":
		if tag == "NN":
			thought = "I think ate is a verb"
			# Past tense of "eat" not the goddess Ate.
			tag = "VBD"

	if thought is not None:
		thought = "Quirkfix: {0}".format(thought)

	return tag, word, thought

