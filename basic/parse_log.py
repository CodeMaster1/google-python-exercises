#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import re

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def get_file_content_as_string(filename):
	opened_file = open(filename, 'rU')
	file_contents = opened_file.read()
	return file_contents

def replace_multi_colons(str):
	count = 0
	while count < 6:
		single_color_str = re.sub(r'::::::', r':::', str)
		str = single_color_str
		count = count + 1
	return str

def parse_log_file(filename):
	file_contents = get_file_content_as_string(filename)
	all_desc = re.sub(r'Description: b[ \'[A-Za-z0-9#,/&\*\+%~><:|?;`\(\)\[\]\-\$!_=\"@.\\[0-9]*]*]*', r':::', file_contents)
	all_desc_1 = re.sub(r'--> Image not liked: Unavailable Page', r':::', all_desc)
	all_desc_2 = re.sub(r'Unavailable Page: b[ \'[A-Za-z#,/&\*\+%~><:|\?;`\(\)\[\]\-!_=\"@.\\[0-9]*]*]*', r':::', all_desc_1)
	all_desc_3 = re.sub(r'\n\n', r'\n', all_desc_2)
	all_desc_4 = re.sub(r'\n', r':::', all_desc_3)
	all_desc_5 = re.sub(r'[\[[0-9]+\/[0-9]+\]]*', r':::', all_desc_4)
	all_desc_6 = replace_multi_colons(all_desc_5)
	all_desc_7 = re.sub(r'Image from: b[ \'[A-Za-z0-9.\-_+=/]*]*:::Number of Followers: [ [0-9]*]*:::--> Image not liked: [ [A-Za-z#,/&\*\+%~><|?`;\(\)\[\]\-!_=\"@.\\[0-9]*]*]*:::', r':::', all_desc_6)
	all_desc_8 = re.sub(r'Image from: b[ \'[A-Za-z0-9.\-_+=/]*]*:::Number of Followers: [ [0-9]*]*:::Link: b\'https://[[A-Za-z0-9.\-_+=/?]*]*\':::--> Already Liked!', r':::', all_desc_7)
	all_desc_9 = re.sub(r'Image from: b[ \'[A-Za-z0-9.\-_+=/]*]*:::Number of Followers: [ [0-9]*]*:::Link: b\'https://[[A-Za-z0-9.\-_+=/?]*]*\':::--> Image not liked: Inappropriate', r':::', all_desc_8)
	all_desc_10 = re.sub(r'Image from: b[ \'[A-Za-z0-9.\-_+=/]*]*:::Number of Followers: [ [0-9]*]*:::Link: b\'https://[[A-Za-z0-9.\-_+=/?]*]*\':::--> Invalid Like Element!', r':::', all_desc_9)
	all_desc_11 = replace_multi_colons(all_desc_10)
	all_desc_12 = re.sub(r'Number of Followers: [ [0-9]*]*', r':::', all_desc_11)
	all_desc_13 = re.sub(r'Link: b\'https://[[A-Za-z0-9.\-_+=/?]*]*\'', r':::', all_desc_12)
	all_desc_14 = re.sub(r'--> Image Liked!', r':::', all_desc_13)
	all_desc_15 = re.sub(r'--> Not following', r':::', all_desc_14)
	all_desc_16 = replace_multi_colons(all_desc_15)
	all_desc_17 = re.sub(r'Image from: b\'[ [A-Za-z.0-9\-_+=/]*]*\':::--> Not commented', r':::', all_desc_16)
	all_desc_18 = re.sub(r'--> Commented: b\'[ [A-Za-z#,/&\*\+%~><:|?;\(\)\[\]\-!_=\"@.\\[0-9]*]*]*\'', r':::', all_desc_17)
	all_desc_19 = re.sub(r'Image from: b', r':::', all_desc_18)
	all_desc_20 = replace_multi_colons(all_desc_19)
	all_desc_22 = all_desc_20.split(':::')
	all_str = ""
	last_element = all_desc_22[-1]
	if all_desc_22[-1] == "":
		last_element = all_desc_22[-2]
	for ele in all_desc_22:
		if ele != "":
			new_ele = re.sub(r'\'', r'"', ele, 1)
			new_ele_2 = re.sub(r'\'', r'": 1', new_ele)
			if ele != last_element:
				all_str = all_str + new_ele_2 + ", "
			else:
				all_str = all_str + new_ele_2
		
	print all_str
# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
	if len(sys.argv) != 2:
		print 'usage: ./parse_log.py file'
		sys.exit(1)
	filename = sys.argv[1]
	parse_log_file(filename)
	
if __name__ == '__main__':
  main()
