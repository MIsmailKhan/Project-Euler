from __future__ import division
import time
import math
import itertools
start = time.time()


def sum_digits(number):
	return sum([int(x) for x in str(number)])
'''
# Brute Force Solution, does not produce required sequence

def is_power_sum(sum_digits,number):
	if number%sum_digits == 0 and sum_digits > 1:
		power = math.log(number)/math.log(sum_digits)
		if power.is_integer() and sum_digits**power == number:
			print(sum_digits,power)
			return True
	return False

def main():
	begin = 512
	nth_term = 2
	while nth_term != 11:
		if is_power_sum(sum_digits(begin),begin):
			print(begin,nth_term )
			nth_term += 1
		begin += 1

	return begin,nth_term
'''

# https://blog.dreamshire.com/project-euler-119-solution/
def main():
	a = []
	n = 30
	for b in range(2, 100):
		for e in range(2, 10):
			p = b ** e
			if sum_digits(p) == b: a.append(p)

	a.sort()
	return a[n - 1]


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))