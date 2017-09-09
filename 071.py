import time
import math
start = time.time()

 # http://www.mathblog.dk/project-euler-71-proper-fractions-ascending-order/

def main():
	a = 3
	b = 7
	r = 0
	s = 1
	limit = 1000000;
	 
	for q in xrange(limit,2,-1):
	    p = ((a*q) - 1)/b
	    if (p*s) > (r*q):
	        s = q
	        r = p

	return r,s
 

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))