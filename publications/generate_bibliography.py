#!/usr/bin/python

# convert bibliography to a collection
# TODO: if this was a Ruby script, this could probably be run automatically when building the site

# read contents of entire file
f = open('bibliography.bib', 'r')
whole_file = f.read()

# split into chunks, each supposedly containing a single reference
bib_array = whole_file.split('\n@')

# make metadata array of size len(bib_array)
meta_array = [dict() for k in range(len(bib_array))]

# get authors of each file
for element in bib_array:
	author = element.split("Author = {",1)[1].split("},\n",1)[0]
	print(author)
