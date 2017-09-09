from __future__ import division

import time
import math
start = time.time()
# Brute Force soln

'''
In order to minimize this we need to maximize the denominator.
As we can see every time we add a distinct prime factor the denominator gets smaller.
So we are looking for a number with as few and as large distinct prime factors as possible.
'''
def is_prime(n):
    # n = abs(n)
    if n<=1: 
        return False
    for i in range(2,(int(math.sqrt(n))+1)):
        if n%i == 0:
            return False
            break
    return True

prime_list = [2]
for i in xrange(3,200000,2):
	if is_prime(i):
		prime_list.append(i)

def totient(n):
	multiplier = 1
	for prime in prime_list:
		if prime > n:
			break
		if n%prime == 0:
			multiplier *= (1-(1/prime))
	return int(n*multiplier)

def is_permutation(n,m):
	if len(str(n)) == len(str(m)):
		digits_n = sorted(list(digit_n for digit_n in str(n)))
		digits_m = sorted(list(digit_m for digit_m in str(m)))
		return digits_m == digits_n
	return False

def main():
	min_ratio = 100
	result = 0
	for i in xrange(4000000,10**7,2):
		print(i)

		if sum(list(int(num) for num in str(i)))%3 == 0:
			continue

		totient_i = totient(i)
		if is_permutation(i,totient_i) and ((i/totient_i) < min_ratio):
			min_ratio = i/totient_i
			result = i

	return  result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) 
