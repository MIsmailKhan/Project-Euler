import time
import math
import itertools
start = time.time()

def read_data(path):

	file = open(path,mode='r').read() #read converts the read object into a string
	data =  filter(None,list(file.split('\n'))) #Filter: Removing any null entries
	all_sets = list()
	for row in data:
		all_sets.append(map(int,list(row.split(','))))

	return filter(None,all_sets)

def test_1(test_1_B,test_1_C):
	return sum(test_1_B) != sum(test_1_C)

def test_2(test_2_B,test_2_C):
	length_B = len(test_2_B)
	length_C = len(test_2_C)
	bigger =  max(length_B,length_C)
	if bigger == length_B:
		return sum(test_2_B) > sum(test_2_C)
	else:
		return sum(test_2_B) < sum(test_2_C)

def test_A(set_a):
	count = 0

	i = 1
	max_size_b = len(set_a)
	while i < max_size_b:
		possible_sets = list(itertools.combinations(set_a, i))
		for set_b in possible_sets:
			print(set_b)

		i += 1

	return True


def main():
	n = list(range(1,4+1))
	print(n)
	return test_A(set(n))

	return sum_result,correct_sets
	
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #5.6s