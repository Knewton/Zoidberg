#!/usr/bin/env python
from argparse import ArgumentParser, FileType
from sys import exit, stdout
from problem import Problem

def argparser():
	desc = "Solves word problems."
	parser = ArgumentParser(description=desc)
	parser.add_argument("--input", type=FileType("r"), default="-",
						help="The question to solve")
	parser.add_argument("--output", default=stdout, type=FileType("w"),
						help="The output file. Defaults to stdout")
	parser.add_argument("--debug", action="store_true", default=True,
						help="Display debugging information")
	return parser

def main():
	args = argparser().parse_args()
	p = Problem(args.input.read(), debug=args.debug)
	p.solve()
	args.output.write(str(p))

if __name__ == "__main__":
	main()

