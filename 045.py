import time
import math
import itertools

start = time.time()

def triangle_numbers(index):
	result = []
	for n in xrange(1,index): 
		result.append((n*(n+1))/2)
	return result

def pentagonal_numbers(index):
	result = []
	for n in xrange(1,index): 
		result.append((n*(3*n-1))/2)
	return result

def hexagonal_numbers(index):
	result = []
	for n in xrange(1,index): 
		result.append(n*(2*n - 1))
	return result

def main():	

	result = set()
	n = 4
	while(len(result)<3):

		length = 10**n
		a = triangle_numbers(length)
		b = pentagonal_numbers(length)
		c = hexagonal_numbers(length)
		
		result = set(a) & set(b) & set(c)
		n += 1
	return result

	'''
	# proposal 1 
	for i,triangle in enumerate(a):
		print("b is {}".format(b[:i+1]))
		for j,pentagon in enumerate(b[i:i+1]):
			print("c is {}".format(c[j:j+1]))
			for hexagon in c[:j+1]:
				if (hexagon in a) and (hexagon in b):
					result.add(hexagon)

	return result
	'''

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))