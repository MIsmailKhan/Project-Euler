import time
import math
import itertools
start = time.time()

def is_prime(n):
	# n = abs(n)
	if n<=0 or n==1: #tweak only for this code, mathematically unsound
		return False
	for i in range(2,(int(math.sqrt(n))+1)):
		if n%i == 0:
			return False
			break
	return True

def permutations(n):
	num = str(n)
	permutes = map(int,[''.join(i) for i in itertools.permutations(num)])
	return permutes

def constant_difference(n,difference,how_many):
	no_of_cases = set()
	for a in n: 
		for b in n:
			if abs( a - b ) == difference:
				no_of_cases.add(a)
				no_of_cases.add(b)

	if len(no_of_cases) >= how_many:
		print(no_of_cases)
		return no_of_cases
	else:
		return False

def main():
	result = set()

	generate_primes= []
	for i in xrange(1000,10000):
		if '0' in str(i):
			continue
		if is_prime(i):
			generate_primes.append(i)

	for prime in generate_primes:

		test = permutations(prime)
		for element in test:
			if not is_prime(element):
				test.remove(element)
		test = sorted(test)

		no_of_cases = 0
		for a in test:
			for b in test:
				if (a - b) == 3330:
					no_of_cases += 1

		if no_of_cases >2:
			result.add(prime)

	return result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))