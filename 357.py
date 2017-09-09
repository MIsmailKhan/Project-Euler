Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.

import math
import time
start = time.time()


def factors(n):
	result = []
	for i in range(2,(n//2)+1):

		if i in result:
			break

		if n%i == 0:
			result.extend((i,(n/i)))

	result.append(n)
	result = list(set(result))
	return result

def is_prime(n):
	# n = abs(n)
	if n<=0 or n==1: #tweak only for this code, mathematically unsound
		return False
	for i in range(2,(int(math.sqrt(n))+1)):
		if n%i == 0:
			return False
			break
	return True

def main():
	for i in xrange(2,100000001):
		test = factors(i)
		for entry in factors:
			if (entry + i)/

elapsed = time.time() - start
print ("%s found in %s seconds" % (solution,elapsed)) 