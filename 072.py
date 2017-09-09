from __future__ import division

import time
import math
start = time.time()

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
for i in xrange(3,1000000+1,2):
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

def main():
	result = 0
	for i in xrange(2,1000000+1):
		print(i)
		result += totient(i)

	return (result)

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # Finished in 2020s ~33 min