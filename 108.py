import time
import math
start = time.time()

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
			
		result.append(power) #[prime_factor,power]

	return result

def main():
	n = 10
	while(True):
		if not is_prime(n): # ensuring that the number isn't a prime
			prime_powers = prime_factors_powers(n)
			powers_n2 = map(lambda x: 2*x + 1, prime_powers)
			factors_n2 = reduce(lambda a, b:a*b, powers_n2)
			unique_solns = (factors_n2 + 1)/2

			if unique_solns > 1000:
				return n

		n += 1

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # 32s