import time
import math
import operator
start = time.time()

def factors(n):
	result = []
	for i in range(2,(n//2)+1):

		if i in result:
			break

		if n%i == 0:
			result.extend((i,(n/i)))

	# result = list(set(result))
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

def prime_factors(n):
	a  = factors(n)
	a.append(n)

	result = []
	for i in a: 
		if is_prime(i):
			result.append(i)

	return set(result)

def main():
	dict_radicals = list()
	for i in xrange(1,100000+1):

		radical = 1
		prime_list = prime_factors(i)
		for element in prime_list:
			radical = radical*element

		dict_radicals.append([i,radical])
		
	list_radicals = sorted(dict_radicals,key=operator.itemgetter(1),reverse=False)
	return list_radicals[9999]



elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # 78.8s