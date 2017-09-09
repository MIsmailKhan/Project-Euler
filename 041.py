import time
import math
import itertools

start = time.time()

def is_prime(n):
	# n = abs(n)
	for i in range(2,(int(math.sqrt(n))+1)):
		if n%i == 0:
			return False
			break
	return True

def main():
	result = 0 
	for n in xrange(10,1,-2): # -2 because 8,5,3 n area divisible by 3
		to_permute = ''.join(map(str,list(reversed(range(1,n)))))
		possibilities = map(int,[''.join(i) for i in itertools.permutations(to_permute)])
		possibilities.sort(reverse=True)
		for entry in possibilities:
			if is_prime(entry):
				return entry

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #1.90734863281e-06 s

