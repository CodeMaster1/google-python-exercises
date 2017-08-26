#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dirs):
	special_paths = []
	for dir in dirs:
		filenames = os.listdir(dir)
		for filename in filenames:
			file_match = re.search(r'__(\w+)__', filename)
			if file_match:
				special_paths.append( os.path.abspath(filename))
	return special_paths

def copy_files(paths, dir):
	if not os.path.exists(dir):
		os.mkdir(dir)
	for file_path in paths:
		file_name = os.path.basename(file_path)
		shutil.copy(file_path, os.path.join(dir, file_name))

def zip_to(paths, zippath):
	
	
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
	args = sys.argv[1:]
	if not args:
		print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
		sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
	todir = ''
	if args[0] == '--todir':
		todir = args[1]
		del args[0:2]

	tozip = ''
	if args[0] == '--tozip':
		tozip = args[1]
		del args[0:2]

	if len(args) == 0:
		print "error: must specify one or more dirs"
		sys.exit(1)

	special_paths = get_special_paths(args)
	
	dir_path = "copied_files_2"
	abs_dir_path = os.path.abspath(dir_path)
	copy_files(special_paths, abs_dir_path)
		
	##zip_to(special_paths, tozip)
	## Zip Utility nor present
  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
