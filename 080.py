from decimal import *
import math 
import time
start = time.time()

getcontext().prec = 102

def digital_sum(n):
	return sum(list(int(digit) for digit in n))

def main():
	
	result = 0
	for i in xrange(1,100): 
		if i in [1,4,9,16,25,36,49,64,81,100]: #all squares under 100
			continue
		else:
			num = str(Decimal(i).sqrt())
			decimal_pos = num.index('.')
			decimal_places = num[decimal_pos+1:-1]
			# print(i)

			result += digital_sum(decimal_places)

	return result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))