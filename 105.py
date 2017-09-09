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
	i = 1
	max_size_b = len(set_a)//2
	while i <= max_size_b:
		# print(i,max_size)
		possible_sets_b = [set(x) for x in itertools.combinations(set_a, i)]
		for set_b in possible_sets_b:

			j = 1
			elements_c  = set_a - set_b
			max_size_c = len(elements_c)
			while j <= max_size_c:
				possible_sets_c = [set(x) for x in itertools.combinations(elements_c, j)]
				for set_c in possible_sets_c:
					if test_1(set_b,set_c):
						if len(set_b) != len(set_c):
							if test_2(set_b,set_c):
								continue
							else:
								return False
						else:
							continue
					else:
						return False
				j += 1
		i += 1

	return True


def main():
	sum_result = 0
	given_sets = read_data('p105_sets.txt')
	count  = 1
	correct_sets = []
	for index,test_set in enumerate(given_sets):
		# print(test_set)
		if len(test_set) != len(set(test_set)):
			continue
		if test_A(set(test_set)):
			sum_result += sum(test_set)
			correct_sets.append(index)

	return sum_result,correct_sets
	
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #5.6s
