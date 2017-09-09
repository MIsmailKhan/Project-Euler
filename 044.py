import time
import math
import itertools
import numpy as np

# Inefficient solution, must improve

start = time.time()

def pentagonal_numbers(index):
	result = []
	for n in xrange(1,index): 
		result.append((n*(3*n-1))/2)
	return result

def main():
	length = 2500
	pentagonal_num = pentagonal_numbers(2*length)
	diff_result = 10000000

	for i,first in enumerate(pentagonal_num):
		for second in xrange(i+1,length):
			add = pentagonal_num[second] + first
			diff = pentagonal_num[second] - first
			if (add in pentagonal_num) and (diff in pentagonal_num):
				if (diff < diff_result):
					diff_result = diff
		# print(i)

	return diff_result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #149.7s

