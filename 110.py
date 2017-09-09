import time
import math
start = time.time()

'''
# Brute force solution

def prime_factors(n):
	result = []
	for i in range(2,int(math.sqrt(n))+1):
		if is_prime(i):
			if i in result:
				break

			if n%i == 0:
				result.append(i)
		else:
			continue

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

def prime_factors_powers(n):
	factors_n = prime_factors(n)
	result = list()
	for prime_factor in factors_n:

		power = 0
		number_copy = n
		while number_copy%prime_factor == 0:
			power += 1
			number_copy = number_copy/prime_factor
		result.append([prime_factor,power])
	return result

def sieve(n):
    not_prime = []
    # prime = []
    for i in xrange(2, n+1):
        if i not in not_prime:
            # prime.append(i)
            for j in xrange(i*i, n+1, i):
                not_prime.append(j)
    return not_prime

# Brute force, maths solved on paper
def main():
	list_numbers = sieve(200000)
	for n in list_numbers:
		print(n)
		distinct_solutions = len(factors(n**2))//2
		if  distinct_solutions > 1000:
			return n
		else:
			n += 1


print(prime_factors_powers(24))
elapsed = time.time() - start
# print ("%s found in %s seconds" % (main(),elapsed)) 
'''