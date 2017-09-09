import math 
import time
start = time.time()

def pentagonal_numbers(index):
	result = {}
	for n in xrange(-index,index): 
		if n == 0:
			continue
		result[n] = (n*(3*n-1))/2

	return result

def n_values(limit):
	result = []
	for i in xrange(1,limit):
		result.append(i)
		result.append(-i)
	return result

max_number = 1000000
pentagonal_dict = pentagonal_numbers(max_number)
dict_ways_to_pile = {0:1, 1:1, 2:2, 3:3, 4:5, 5:7, 6:11, 7:15, 8:22, 9:30}
indexes = n_values(max_number)

def ways_to_pile(n):
	if n in dict_ways_to_pile.keys():
		return dict_ways_to_pile[n]
	else:
		i = 0
		result = 0
		while(n - pentagonal_dict[indexes[i]] >= 0): #n_values is used for obtaining the value of m
			sign = (-1)**(abs(indexes[i])-1) # n_values[i] is m 
			entry = n - pentagonal_dict[indexes[i]]
			
			result += (sign * ways_to_pile(entry))
			i += 1

		dict_ways_to_pile[n] = result
		return result

def main():
	for i in xrange(1,max_number):
		test = ways_to_pile(i)
		print(i,test)
		if test%1000000 == 0:
			return i

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))


'''
from itertools import *
import math 
import time
start = time.time()


def pentagonal(n):
    return n*(3*n - 1) / 2

partitions = {}
generalized_pentagonals = sorted(map(pentagonal, list(range(-250, 250))))[1:]
def partition(n):
    if n <= 1: return 1
    if n not in partitions:
        signs = cycle([1, 1, -1, -1])
        pentagonals = takewhile(lambda p: p <= n, generalized_pentagonals)
        partitions[n] = sum(sign * partition(n - p) for sign, p in zip(signs, pentagonals))

    return partitions[n]

def main():
    print(next((n for n in count(0) if partition(n) % 1000000 == 0)))

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))
'''