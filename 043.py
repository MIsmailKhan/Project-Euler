import time
import math
import itertools
start = time.time()

def permutations(n):
	num = str(n)
	permutes = [''.join(i) for i in itertools.permutations(num)]
	return permutes

def substring_divisibility(string_number):
	primes = [0,2,3,5,7,11,13,17]
	for i in xrange(1,8):
		sub_string = int(string_number[i:i+3])
		# print(i,sub_string)
		if (sub_string % primes[i]) == 0:
			continue
		else:
			return False

	return True

def main():
	test_cases = permutations(9876543210)
	sum_result = 0
	for test_case in test_cases:
		if substring_divisibility(test_case):
			sum_result = sum_result + int(test_case)

	return sum_result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))




