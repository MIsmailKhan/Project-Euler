import time
import math

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
for i in xrange(1,20000):
	if is_prime(i):
		prime_list.append(i)	

def sum_consecutive(start,stop):
	return sum(prime_list[start:stop])

def main():
	test_length = 536 
	result = 0
	for begin in xrange(0,len(prime_list)-1):
		for end in xrange(begin+1,len(prime_list)-1):

			length = end - begin
			check = sum_consecutive(begin,end)
			
			if check >= 1000000:
				break
			else:
				if (length)>test_length and is_prime(check):
					test_length = length
					result = check

	return result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))

