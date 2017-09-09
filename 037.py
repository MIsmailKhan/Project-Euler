import time 
import math
import itertools
start = time.time()

def is_prime(n):
	# n = abs(n)
	if n ==1:
		return False
	for i in range(2,(int(math.sqrt(n))+1)):
		if n%i == 0:
			return False
			break
	return True

def right_truncatable_prime(n):
	while(n!=0):
		if (is_prime(n)):
			n = n//10
		else:
			return False
	return True


def left_truncatable_prime(n):
	while(n!=0):
		if (is_prime(n)):
			power = len(str(n))-1
			n = n%(10**power)
		else:
			return False
	return True

def main():
	count = 0
	total_sum = 0
	i = 9
	while (count<11):
		if left_truncatable_prime(i) and right_truncatable_prime(i):
			count += 1
			total_sum += i
		i += 2
	return total_sum

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))  #9.53674316406e-07 s