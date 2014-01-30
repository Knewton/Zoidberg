#!/usr/bin/env python
from os.path import (expanduser, isdir, exists, join, abspath, splitext,
	basename, dirname)
from os import mkdir, makedirs, listdir
from errno import EEXIST
from subprocess import Popen, PIPE, STDOUT
from types import ListType
from shutil import copyfile
from json import dumps, loads

def ownerize(s):
	if s[-1] == "s":
		return s + "'"
	else:
		return s + "'s"

def oxfordComma(inp):
	o = [] + inp
	outstr = ""
	if len(o) > 1:
		laststr = o.pop()[0]
		o = [i[0] for i in o]
		outstr = ", ".join(o)
		outstr += " and {0}".format(laststr)
	else:
		return o[0]
	return outstr

def list_format(orig):
	# Copy the list to not disrupt it
	l, o = [], []
	l.extend(orig)

	if len(l) > 2:
		last = l.pop()
		o.append(", ".join(l) + ",")
		o.append(last)
	elif len(l) > 0:
		o = l

	if len(o):
		return " and ".join(o)
	return None

def mkdirp(path):
	try:
		makedirs(path)
	except OSError as exc: # Python >2.5
		if exc.errno == EEXIST:
			pass
		else: raise

def read_file(file_path):
	with open(fix_path(file_path), 'r') as f:
		data = f.read()
	return data

def write_file(file_path, content, mode="w"):
	with open(fix_path(file_path), mode) as stream:
		stream.write(content)

def get_json(fp):
	try:
		return loads(read_file(fp))
	except ValueError:
		return None

def set_json(fp, content, mode="w"):
	try:
		return write_file(fp, dumps(content), mode)
	except ValueError:
		return None

def call(command, exit_on_failure=False):
	if type(command) == ListType:
		command = " ".join(command)
	process = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True)
	print process.communicate()[0]
	code = process.returncode
	if exit_on_failure:
		if code != 0:
			exit(1)
	return code

def fix_path(p):
	return abspath(expanduser(p))

def copy_missing_files(src, dest, force, underscore=False):
	if not isdir(dest):
		mkdir(dest)

	had_file = False
	for f in listdir(src):
		fp = join(src, f)

		# Replace underscore with dot
		if underscore and f[0] == "_":
			dest_fp = ".{0}".format(f[1:])
		else:
			dest_fp = join(dest, f)

		if isdir(fp):
			if copy_missing_files(fp, join(dest, f), force, underscore):
				had_file = True
		else:
			if exists(dest_fp) and not force:
				continue
			print "Adding {0}".format(dest_fp)
			copyfile(fp, dest_fp)
			had_file = True
	return had_file

def merge_directories(src, dest, dirs=None, force=False, underscore=False):
	src = fix_path(src)
	dest = fix_path(dest)
	made_change = False

	if not isdir(src):
		return False

	if not isdir(dest):
		mkdir(dest)

	if dirs is None:
		return copy_missing_files(src, dest, force, underscore)

	for d in dirs:
		if copy_missing_files(join(src, d), join(dest, d), force, underscore):
			made_change = True
	return made_change

def create_archive_basedir(file_path):
	"""Given an archive, creates a sibling directory for clean checkout"""
	file_name, ext = splitext(basename(file_path))
	basedir = join(dirname(file_path), file_name)

	if not isdir(basedir):
		makedirs(basedir)

	return basedir

def unzip(archive, path):
	from zipfile import ZipFile
	z = ZipFile(archive, "r")
	z.extractall(path)

def untar(archive, path):
	from tarfile import TarFile
	t = TarFile(archive, "r")
	t.extractall(path)

class UnknownArchiveException(Exception):
	pass

def unpackage(file_path, package_type=None):
	"""Unpackages an archive into a sibling directory of the same name."""
	if package_type is None:
		if ".tar" in file_path:
			package_type = "tar"
		else:
			file_name, ext = splitext(file_path) # foo.txt -> (foo, .txt)
			package_type = ext[1:] # Remove the . from .txt

	# Create a sibling directory for extraction
	basedir = create_archive_basedir(file_path)

	# Handle the extraction
	if package_type == "zip":
		unzip(file_path, basedir)
	elif package_type == "tar":
		untar(file_path, basedir)
	else:
		raise UnknownArchiveException(package_type)

	# Return the destination
	return basedir

def uniq(l):
	return list(sorted(set(l), key=l.index))

def output_tuples(src, o, l, frmt=False):
	for tuples in src:
		words, tags = [], []
		index = 0
		for tup in tuples:
			word = tup[0]
			tag = tup[1]

			# Sometimes our values are packed in tuples
			if not isinstance(word, basestring):
				if word[0] is not None:
					word = word[0]
				else:
					word = word[1]

			if index == 0 and tag != "context":
				word = word.capitalize()

			words.append("{: <{l}}".format(word, l=l))
			tags.append("{: <{l}}".format(tag, l=l))
			index += 1
		# Add 4 spaces for preformatted in markdown
		o.append("    " + ("\t".join(words)))
		o.append("    " + ("\t".join(tags)))
		o.append("")

