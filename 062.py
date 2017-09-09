import math 
import time
import itertools 
start = time.time()
# Brute Force : Slow solution >5 minutes
# Alternate solution: for every cube number , generate digits and compare with every number's digits in cube list - runs in 2s 

def digits(n):
	return map(int,list(i for i in str(n))) #returns list containing the digits in int data type

def digit_root(n):
	n_digits = digits(n) 
	n_digits = filter(lambda a: a != 9, n_digits) #remove all instances of 9 since 9 doesn't affect the digit root
	sum_digits = sum(n_digits)
	while len(str(sum_digits)) > 1:
		sum_digits = sum(digits(sum_digits)) # computes digit sum till single digit answer is reached
	return sum_digits

def permutations_n(n):
	num = str(n)
	permutes = map(int,[''.join(i) for i in itertools.permutations(num)])
	return permutes

def cubic_numbers(end,begin=1):
	return list(n**3 for n in xrange(begin,end))

def is_perfect_cube(n):
    # x = abs(n)
    return int(round(n ** (1. / 3))) ** 3 == n

def main():
	generate_cubes = cubic_numbers(10000,300)
	for number in generate_cubes:
		
		count_cubes = 0
		possibilities = set(permutations_n(number)) 
		#set required because it cannot differentiate between 41063625 and 41063625, the two sixes are treated as unique digits,hence the issue
		possibilities = filter(lambda x: len(str(x)) == len(str(number)) , possibilities) 
		#remove all permutations not having same digits as number
		for entry in possibilities:
			if digit_root(entry) in [1,8,9]:
				if is_perfect_cube(entry):  # entry**(1./3)).is_integer(): Does not work, returns False as the calculations returns non-terminating value 344.99999.....
					count_cubes += 1
		print(number)
		if count_cubes == 5:
			return number 

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #

'''
# too slow
if entry in generate_cubes:
	list_cubes.append(entry)
	count_cubes += 1
else:
	continue
'''
