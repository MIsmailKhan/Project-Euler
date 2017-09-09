import math
import time
start = time.time()

def is_integer(l,wh):
	shortest_path = float((l**2 + (wh)**2)**0.5)
	return shortest_path.is_integer()

def main():
	count = 0
	target = 1000000
	for length in xrange(2,10000):
		for weight_height in xrange(3,2*length):

			if is_integer(length,weight_height):
				weight_height_possibilities = weight_height//2
				count += (weight_height / 2) if weight_height <= length else (1 + (length - (weight_height+1)/2))

		if count >= target:
			return length 
			
	return "None found"


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))
