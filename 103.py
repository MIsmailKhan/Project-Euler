import time
import math
import itertools
start = time.time()

special_sum_sets = {1:[1],2:[1,2],3:[2,3,4],4:[3,5,6,7],5:[6,9,11,12,13],6:[11, 18, 19, 20, 22, 25]}

def near_optimum_set(n): #Based on formula
	length_previous = len(special_sum_sets[n-1])
	previous_set = special_sum_sets[n-1]
	b = previous_set[length_previous//2]  

	result = [b]
	i = 0
	while i < length_previous:
		result.append(previous_set[i] + b)
		i += 1

	# special_sum_sets[n] = result
	return result

def test_1(B,C):
	return sum(B) != sum(C)

def test_2(B,C):
	length_B = len(B)
	length_C = len(C)
	bigger =  max(length_B,length_C)
	if bigger == length_B:
		return sum(B) > sum(C)
	else:
		return sum(B) < sum(C)

def test_A(set_a):
	i = 1
	max_size = len(set_a)//2
	while i <= max_size:
		possible_sets = [set(x) for x in itertools.combinations(set_a, i)]
		for set_b in possible_sets:
			set_c  = set_a - set_b
			if test_1(set_b,set_c) and test_2(set_b,set_c):
				continue
			else:
				return False
		i += 1

	return True

# Assume that the optimum set lies in the region of +/- 3 of the values of the near optimum set
def main(): 
	current_best = near_optimum_set(7) # list is useful when checking for occurences greater than 1 in  the list
	current_best_sum = sum(current_best)

	# The missing puzzle piece: how to get all possible sets in range -3 and +3 of near optimum
	# https://bartriordan.wordpress.com/2014/04/16/project-euler-problem-103-solution/
	for test_tuple in itertools.product(*[list(range(x - 3, x + 4)) for x in current_best]):
	 	if sum(test_tuple) >= current_best_sum:
	   		continue
		elif len(test_tuple) != len(set(test_tuple)): #checking if entries are unique
			continue
		elif test_A(set(test_tuple)):
			current_best = set(test_tuple)
	        current_best_sum = sum(test_tuple)
        else:
        	pass

	return current_best

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))
