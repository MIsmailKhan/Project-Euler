import time
import math
from itertools import permutations
start = time.time()

# Fairly verbose solution
# Note: Create functions to create more elegant code

def triangle_numbers(index,start=1):
	result = []
	for n in xrange(start,index): 
		result.append((n*(n+1))/2)
	return result

def square_numbers(index,start=1):
	return [n**2 for n in range(start,index+1)]

def pentagonal_numbers(index,start=1):
	result = []
	for n in xrange(start,index): 
		result.append((n*(3*n - 1))/2)
	return result

def hexagonal_numbers(index,start=1):
	result = []
	for n in xrange(start,index): 
		result.append(n*(2*n - 1))
	return result

def heptagonal_numbers(index,start=1):
	result = []
	for n in xrange(start,index): 
		result.append((n*(5*n - 3))/2)
	return result

def octagonal_numbers(index,start=1):
	result = []
	for n in xrange(start,index): 
		result.append(n*(3*n - 2))
	return result


def main():
	triangle = triangle_numbers(141,45)
	square = square_numbers(99,32)
	pentagonal = pentagonal_numbers(82,26)
	hexagonal = hexagonal_numbers(71,23)
	heptagonal = heptagonal_numbers(64,21)
	octagonal = octagonal_numbers(59,19)
	perms = list(permutations([triangle,square,pentagonal,hexagonal,heptagonal,octagonal]))

	for perm in perms:
		for entry_0 in perm[0]:
			for entry_1 in perm[1]:
				if str(entry_0)[-2:] == str(entry_1)[:2]:
					for entry_2 in perm[2]:
						if str(entry_1)[-2:] == str(entry_2)[:2]:
							for entry_3 in perm[3]:
								if str(entry_2)[-2:] == str(entry_3)[:2]:
									for entry_4 in perm[4]:
										if str(entry_3)[-2:] == str(entry_4)[:2]:
											for entry_5 in perm[5]:
												if str(entry_4)[-2:] == str(entry_5)[:2] and str(entry_5)[-2:] == str(entry_0)[:2]:
													print(entry_0,entry_1,entry_2,entry_3,entry_4,entry_5)
													return (entry_0 + entry_1 + entry_2 + entry_3 + entry_4 + entry_5)

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #0.1s
