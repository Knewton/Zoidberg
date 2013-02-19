#!/usr/bin/env python
from argparse import ArgumentParser, FileType
from zoidberg.problem import Problem
from sys import exit, stdout

def argparse():
	desc = "Solves word problems."
	parser = ArgumentParser(description=desc)
	parser.add_argument("--input", type=FileType("r"), default="-",
						help="A single question to solve")
	parser.add_argument("--brain", type=str, default="~/.zoidberg.brain.json",
						help="The brain to use for solving")
	parser.add_argument("--output", default=stdout, type=FileType("w"),
						help="The output file. Defaults to stdout")
	return parser

def main():
	args = argparse().parse_args()

	p = Problem(args.input.read(), args.brain)
	p.solve()
	args.output.write(str(p) + "\n")

	exit(0)

if __name__ == "__main__":
	main()
