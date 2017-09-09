from __future__ import division

import time
import math
start = time.time()

def main():
	n = math.pow(10,12)
	while(True):
		x  = (1 + (1+(2*n*(n-1)))**0.5)/2
		if x.is_integer():
			print(x)
		n += 1

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #0.0s