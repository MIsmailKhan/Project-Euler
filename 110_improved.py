import time
import math
start = time.time()

not_prime_list = set()

def is_prime(n):
	# n = abs(n)
	if n<=0 or n==1: #tweak only for this code, mathematically unsound
		return False
	for i in range(2,(int(math.sqrt(n))+1)):
		if n%i == 0:
			not_prime_list.add(i)
			return False
	return True

limit = 50000000
prime_list = [2]
for i in xrange(3,int(math.sqrt(limit)),2):
	if is_prime(i):
		prime_list.append(i)



def prime_factors(n):
	result = []
	for i in range(2,int(math.sqrt(n))+1):
		if i in prime_list:
			if i in result:
				break

			if n%i == 0:
				result.append(i)
		else:
			continue

	return result

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
	n = 180180 # We know that any number below this has less tahn 1000 unique solutions
	while(True):
		if i in not_prime_list: # ensuring that the number isn't a prime
			print(i)
			prime_powers = prime_factors_powers(n)
			powers_n2 = map(lambda x: 2*x + 1, prime_powers)
			factors_n2 = reduce(lambda a, b:a*b, powers_n2)
			unique_solns = (factors_n2 + 1)/2

			if unique_solns > 4000000:
				return n

		n += 1

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) 