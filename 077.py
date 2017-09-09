import math 
import time
start = time.time()

def is_prime(n):
	# n = abs(n)
	if n<=0 or n==1: 
		return False
	for i in range(2,(int(math.sqrt(n))+1)):
		if n%i == 0:
			return False
			break
	return True

prime_list = []
for i in xrange(1,2000):
	if is_prime(i):
		prime_list.append(i)

def permutations_number(n):
	target = n
	numbers = sorted(prime for prime in prime_list if prime < n)
	ways = [1] + [0]*target

	for number in numbers:
	    for i in xrange(number, target+1):
	        ways[i] += ways[i-number]
	return ways[target]
	
def main():
	test_number = 10
	while(permutations_number(test_number) <= 5000):
		print(test_number)
		test_number += 1

	return test_number

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # 0.0s