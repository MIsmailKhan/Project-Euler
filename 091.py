import math
import time
start = time.time()

def gcd(m, n):
	while m % n != 0:
		old_m = m
		old_n = n

		m = old_n
		n = old_m % old_n
	return n

def main():
	size = 50;
	result = size*size*3;
	for x in xrange(1,size+1):
		for y in xrange(1,size+1):
			fact = gcd(x, y)
			result += min(y*fact /x, (size - x)*fact /y) * 2
    
	return result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # 0.0s