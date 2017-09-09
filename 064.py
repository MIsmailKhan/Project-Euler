import math
import time
start = time.time()

def sequence(n):
	period_result = 0
	m = 0
	d = 1
	a0 = int(math.sqrt(n))
	a = a0
	if a0 != math.sqrt(n):
		while( a != 2*a0):
			m = a*d - m
			d = (n  - m**2)//d
			a = (a0 + m)//d
			print(a)
			period_result += 1

	# return period_result
		
def main():
	result_count = 0
	for i in xrange(2,10000):
		print(i,sequence(i))
	return result_count

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))






