import math 
import time
start = time.time()

# http://www.mathblog.dk/project-euler-75-lengths-of-wire-right-angle-triangle/
# https://en.wikipedia.org/wiki/Pythagorean_triple

def gcd(m, n):
	while m % n != 0:
		old_m = m
		old_n = n

		m = old_n
		n = old_m % old_n
	return n

def main(max_perimeter):
	results = set()
	count_results = 0
	for m in xrange(2,int(math.sqrt(max_perimeter/2))+1,2):
		for n in xrange(1,m,2):
			if gcd(n,m) == 1:
				a = m**2 - n**2
				b = 2 * m * n
				c = m**2 + n**2

				results.add(a+b+c)
			else:
				continue

	return len(results)
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(1500000),elapsed))