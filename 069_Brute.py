from __future__ import division

#Brute Force algorithm
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
	euler_totient = []
	for i in xrange(2,1000000):
		relatively_prime = []
		for number in xrange(1,i):
			if gcd(i,number) == 1:
				relatively_prime.append(number)
		euler_totient.append(i/len(relatively_prime))

	return euler_totient.index(max(euler_totient)) + 2


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))