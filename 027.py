import time 
import sys

#Brute Force solution
start = time.time()

def is_prime(n):
	n = abs(n)
	for i in range(2,n//2):
		if n%i == 0:
			return False
			break
	return True

max_count = 41
for a in range(-1000,1000):
	for b in range(-1000,1000):
		count = 0
		for n in xrange(0,sys.maxint):
			formula  = (n**2) + (a*n) + b
			# print(formula)
			if is_prime(formula):
				count += 1
			else:
				break
		#print a,b
		#print count 
		if count > max_count:
			max_count = count
			result= a*b


elapsed = time.time() - start
print ("%s found in %s seconds" % (result,elapsed)) 
