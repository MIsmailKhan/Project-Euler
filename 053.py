import time
from math import factorial

start = time.time()

def combinations(n,r):
	num = 1
	return (factorial(n)/(factorial(r)*factorial(n-r))) #using math.factorial is the fastest way. 

#alternates: REcursion fucntion(P 34) or https://people.eecs.berkeley.edu/~fateman/papers/factorial.pdf

def main():
	result_count = 0
	for n in xrange(0,101):
		for r in xrange(0,n+1):
			if combinations(n,r) > 1000000:
				result_count += 1
	return result_count

elapsed = time.time() - start 
print ("%s found in %s seconds" % (main(),elapsed)) #0.1s
