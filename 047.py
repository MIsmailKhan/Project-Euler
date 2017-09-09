import time
import math
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
	result = []
	for i in a: 
		if len(result)<=4:
			if is_prime(i):
				result.append(i)
	return set(result)

def main():
	num = 2
	while(True):
		print(num)
		if (len(prime_factors(num))==4) and (len(prime_factors(num+1))==4) and (len(prime_factors(num+2))==4) and (len(prime_factors(num+3))==4):
			print("Done")
			return (num,num+1,num+2,num+3)
			break 
		else:
			num += 1

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) 
