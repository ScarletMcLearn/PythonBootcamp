#!/usr/bin/env python
## Imports
import sys
import os
from collections import defaultdict

## Globals
JUSTANEXAMPLE = 'whichdoesnotmakesense'

## Classes
class Person(object):
	def __init__(self):
		self.first_name = None
		self.last_name = None
	
	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)
	
	def set_first_name(self, first_name):
		self.first_name = first_name
	
	def set_last_name(self, last_name):
		self.last_name = last_name

## Functions
def main(first_name, last_name):
	'''main loop'''
	new_person = Person()
	new_person.set_first_name(first_name)
	new_person.set_last_name(last_name)
	print new_person

## Program
if __name__ == '__main__':
	# commandline parameters
	first_name = sys.argv[1]
	last_name = sys.argv[2]

	main(first_name, last_name)
