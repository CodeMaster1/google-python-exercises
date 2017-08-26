#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def get_file_content_as_string(filename):
	opened_file = open(filename, 'rU')
	file_contents = opened_file.read()
	return file_contents

def second_word_sort(url):
	match = re.search(r'-(\w+)-(\w+)\.\w+', url)
	if match:
		return match.group(2)
	else:
		return url
	
def read_urls(filename):
	"""Returns a list of the puzzle urls from the given log file,
	extracting the hostname from the filename itself.
	Screens out duplicate urls and returns the urls sorted into
	increasing order."""
	url_list = {}
	
	file_path = os.path.abspath(filename)
	print file_path
		
	if os.path.exists(file_path) == True:
		file_contents = get_file_content_as_string(file_path)
		
		cat_regex = re.search(r'(\w+)_(\w.+)', filename)
		category = ''
		server_name = ''
		if cat_regex:
			category = cat_regex.group(1)
			server_name = cat_regex.group(2)
		
		split_strs = file_contents.split('\n')
		for split_str in split_strs:
			str_regex = re.search(r'\s(/\w.+?)\s', split_str)
			
			if str_regex:
				url_element = "http://" + server_name + str_regex.group(1)
				all_puzzle_url = re.search(r'.+puzzle.+', url_element)
				
				if all_puzzle_url:
					all_puzzle_url_ele = all_puzzle_url.group()
					if all_puzzle_url_ele in url_list:
						url_list[all_puzzle_url_ele] = url_list[all_puzzle_url_ele] + 1
					else:
						url_list[all_puzzle_url_ele] = 1
					
	sort_url_list = sorted(url_list.keys(), key=second_word_sort)
		
	return sort_url_list

def download_images(img_urls, dest_dir):
	"""Given the urls already in the correct order, downloads
	each image into the given directory.
	Gives the images local filenames img0, img1, and so on.
	Creates an index.html in the directory
	with an img tag to show each local image file.
	Creates the directory if necessary.
  """
	i = 0
	output_file_name = "index.html"
	abs_opf = os.path.abspath(output_file_name)
	output_file = open(abs_opf, 'w')
	output_file.write("<verbatim><html><body>\n")
	for img_url in img_urls:
		local_name = 'img%d.jpg' % i
		print 'Retrieving...', img_url
		urllib.urlretrieve(img_url, os.path.join(dest_dir, local_name))
		output_string = "<img src = \"" +  os.path.join(dest_dir, local_name) + "\">"
		output_file.write(output_string)
		i = i + 1
  # +++your code here+++
	output_file.write("</body></html>")
	
	output_file.close()
		

def main():
	args = sys.argv[1:]

	if not args:
		print 'usage: [--todir dir] logfile '
		sys.exit(1)

	todir = ''
	if args[0] == '--todir':
		todir = args[1]
		del args[0:2]

	img_urls = read_urls(args[0])
	
	todir_abs = os.path.abspath(todir)
	dir_exists = os.path.exists(todir_abs)
	if dir_exists == False:
		os.mkdir(todir_abs)
	
	if todir:
		download_images(img_urls, todir_abs)
	else:
		print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
