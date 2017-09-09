import operator as op
import math
import time
start = time.time()

def combinations(n,r):
	r = min(r, n-r)
	if r == 0: return 1
	numer = reduce(op.mul, xrange(n, n-r, -1))
	denom = reduce(op.mul, xrange(1, r+1))
	return numer//denom

def main():
	closest = 2000000
	for i in xrange(1,1000): # rows in grid
		for j in xrange(1,i): # columns in grid
			no_of_rectangles = combinations(i+1,2) * combinations(j+1,2)
			close_to_2_million = abs(2000000 - no_of_rectangles)

			if closest > close_to_2_million: 
				closest = close_to_2_million
				area = i*j

	return closest,area

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # 0.8s