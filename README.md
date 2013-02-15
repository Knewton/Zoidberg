# Zoidberg
A word problem solver.

# Requirements
* Python 2.7+
* SymPy
* NumPy
* NLTK

# How it works
Zoidberg solves word problems in three distinct steps.

## Interpretation
Zoidberg uses a triple interpretation approach to parse word problems. The raw
text of the word problem is iterated over three times, each cycle of the
iteration designed to pull out or piece together different information about
the problem at hand.

### Solution inference
> What implications does the problem make about itself?

The first analysis of the problem uses the Inference engine to make some quick
judgements on what the problem is about. Without going into any specific detail
about the problem itself, the Inference engine provides some quick and dirty
directionality for the query parser.

For example, a word problem containing the word "another" might be an addition
problem; one containing the word "fewer" might be subtraction. The output of
the inference engine isn't designed to be right, it's designed to be fast.

This step is intended to model the cognitive process of a rough first
impression of the question being asked; it is expected the first impression
will often be wrong or incomplete, but even then should be invaluable to the
query parser for actually targeting the real question.

### Query parsing
> What is the question being asked?

The second analysis of the problem uses the Parsing engine to determine the
question actually being asked. The parser marries the general impressions of
the Inference engine with specifics about the problem itself.

A properly parsed query will be a mathematical formulation of the question
being asked, in symbolic notation, which SymPy could then solve for us.

### Data extraction
> What salient data is proved; what data is missing?

Once the question we need to answer is known, the Extraction engine attempts to
fill in whatever data is missing from our expression such that it can be
properly solved.

The Extractor exclusively uses the query, and attempts only to fill in missing
data from the query. A properly extracted problem will be an expression.

## Solving
Once an expression has been defined, it can be solved. SymPy is used to handle
expression solving. To the best of its abilities, Zoidberg will attempt to
respond with a humanized, textual version of the answer.

An ideal solution is "Jane has 6 balloons" instead of "6" or "6 balloons".

## Learning
Arguably the most important part of the Zoidberg model is the ability to learn
new things. A ~/brain.zoidberg.json file will be created in your home directory
to store learned behaviors.

The learning process is heavily involved in modifying the default functionality
of all it's engines.

# Why is it named Zoidberg?
Need a project name? Why not Zoidberg?

# Tagging reference
PoS Tagging reference list:
    ftp://ftp.cis.upenn.edu/pub/treebank/doc/tagguide.ps.gz

