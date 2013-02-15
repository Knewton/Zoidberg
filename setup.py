#! /usr/bin/env python
from distutils.core import setup
from os import environ, mkdir, symlink
from os.path import expanduser, isdir
from distutils.sysconfig import get_python_lib

setup(
	name="zoidberg",
	description="A word problem solver.",
	author="Eric Garside",
	author_email="eric@knewton.com",
	url="http://github.com/Knewton/Zoidberg",
	packages = ["zoidberg"],
	platforms=["any"],
	data_files=[
		("/usr/local/bin", ["bin/zoidberg"])
	]
)
