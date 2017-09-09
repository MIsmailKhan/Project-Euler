import math 
import time
start = time.time()

def main():
	number = (28433 * pow(2,7830457,10**10)) + 1 
	return str(number)[-10:]

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #0.0s

