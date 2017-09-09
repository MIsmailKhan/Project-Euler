import time
import math
start = time.time()

# Takes too long > 30 minutes

def factors(n):
	result = [1]
	for i in range(2,(n//2)+1):

		if i in result:
			break

		if n%i == 0:
			result.extend((i,(n/i)))

	result = list(set(result))
	return result

def amicable_chain(n):
	chain = [n]
	test = sum(factors(chain[-1]))
	while(len(chain) == len(set(chain))):
		chain.append(test)
		test = sum(factors(chain[-1]))

		if test > 1000000:
			return []

	if chain.count(n) == 2:
		return set(chain)
	else:
		return []

def main():
	i = 10
	longest_chain_length = 0
	for i in xrange(10,1000000):
		amicable_list = amicable_chain(i)
		chain_length = len(amicable_list)

		if chain_length > longest_chain_length:
			longest_chain_length = chain_length
			longest_chain = amicable_list

		print(i)
	
	return min(longest_chain),longest_chain
	

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) 
