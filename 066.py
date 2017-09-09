import math 
import time
start = time.time()

def sequence(D):
	a0 = int(math.sqrt(D))
	if a0 != math.sqrt(D):
		m = 0
		d = 1
		a = a0

		num_prev = 1
		num_current = a

		den_prev = 0
		den_current = 1

		while (num_current**2 - (D*den_current*den_current)) != 1:
			m = (a*d) - m
			d = (D - (m**2))/d
			a = (a0 + m)/d

			num_prev2 = num_prev
			num_prev = num_current
			num_current = (a*num_prev) + num_prev2

			den_prev2 = den_prev
			den_prev = den_current
			den_current = (a*den_prev) + den_prev2

		return num_current

	return -1

def main():
	max_num = 0
	result = 0
	for i in xrange(2,1001):
		test = sequence(i)
		if max_num < test:
			max_num = test
			result = i
	return result
	
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #0.0s

