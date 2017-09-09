import time
import math
start = time.time()

def main():
	sum = 0
	for i in xrange(1,1001):
		sum += i**i
	result = str(int(sum))[-10:]
	return result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))  #9.53674316406e-07 s
