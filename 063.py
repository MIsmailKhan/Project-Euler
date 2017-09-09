import time
import math
start = time.time()
# Note: Create alternative solution
# Need for better understanding of question

def main():
	result = []
	for base in xrange(1,101):
		for power in xrange(1,101):
			num = base**power
			if len(str(num)) == power:
				result.append(power)
				
	return len(result)

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))
