from __future__ import division
from operator import mul
import math
import time 

#This uses fermat's little theorem to solve
start = time.time()
'''
def factors(n):
	result = [1]
	for i in range(2,(n//2)+1):

		if i in result:
			break

		if n%i == 0:
			result.extend((i,int(n/i)))

	result = list(set(result))
	return result

def prime_factors(factors_list):
	prime_list = []
	flag = True
	factors_list.remove(1)
	for i in factors_list:
		if len(factors(i)) == 1: #checking if the factor is a prime factor
			prime_list.append(i)
	return prime_list

to_iterate = []

flag = True
for i in range(2,10000):
	check = prime_factors(factors(i))
	if len(check) == 0: # all prime numbers
		to_iterate.append(i)
	#if len(check)<3 and (reduce(mul, check, 1)==2 or reduce(mul, check, 1)==5 or reduce(mul, check, 1)==10):
	#	continue
	#to_iterate.append(i)

# print to_iterate
	

def recurring_cycle(n, d):
    # solve 10^s % d == 10^(s+t) % d
    # where t is length and s is start
    for t in range(1, d):
        if 1 == 10**t % d:
            return t
    return 0

longest = max(recurring_cycle(1, i) for i in to_iterate)
print([i for i in to_iterate if recurring_cycle(1, i) == longest][0])
'''

elapsed = time.time() - start

#print ("%s found in %s seconds" % (answer,elapsed)) 
