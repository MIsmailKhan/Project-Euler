import time
import math
start = time.time()

def area(a,b):
	height = (b**2 - (0.25 * a**2 ))**0.5
	area = 0.5 * a * height
	if area.is_integer():
		return area
	else:
		return 0

def perimeter(a,b):
	return a + (2*b)

def main():
	sum_perimeters = 0
	for a in xrange(2,333333335):
		if perimeter(a,a+1) > 1000000000:
			continue
		if area(a,a+1) != 0:
			sum_perimeters += perimeter(a,a+1)

		if a%1000000 == 0:
			print(a)
		
	return sum_perimeters

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))

