import math
import time

start = time.time()

set_numbers = set()
for a in xrange(2,100+1):
	for b in xrange(2,100+1):
		set_numbers.add(a**b)

solution = len(set_numbers)

elapsed = time.time() - start
print ("%s found in %s seconds" % (solution,elapsed)) 
