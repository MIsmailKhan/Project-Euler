import math 
import time
start = time.time()

def main():
	target = 10
	numbers = list(range(1,target))
	ways = [1] + [0]*target

	for number in numbers:
	    for i in range(number, target+1):
	        ways[i] += ways[i-number]
	return ways[target]

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))

