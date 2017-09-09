import math
import time
start = time.time()

# SOlution solved on paper
def main():
	r = 0;
	for a in xrange(3,1001):
		r += 2*a*((a-1) / 2)
	return r



elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))