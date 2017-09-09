import time
import math
import itertools
start = time.time()
# Fairly slow solution

def anagram(s1, s2):
	c1 = [0] * 26
	c2 = [0] * 26

	for i in range(len(s1)):
		pos = ord(s1[i]) - ord('A')
		c1[pos] += 1

	for i in range(len(s2)):
		pos = ord(s2[i]) - ord('A')
		c2[pos] +=  1

	j = 0
	still_ok = True
	while j < 26 and still_ok:
		if c1[j] == c2[j]:
			j = j + 1
		else:
			still_ok = False

	return still_ok

def read_data(path):

	file = open(path,mode='r').read() #read converts the read object into a string
	words = list(file.replace('"','').split(',')) 
	return words

def squares(n):
	return list(i**2 for i in xrange(1,n+1))

squares_list = squares(179)

def get_mappings(word):
	letters = set(character for character in word)
	possibilities  = itertools.permutations('0123456789',len(letters))
	all_mappings = []
	for possibility in possibilities:
		mapping = dict(zip(letters,possibility))
		all_mappings.append(mapping)

	return all_mappings
		
def is_square_mapping(anagram_pair,possible_mapping):
	test_pair = list()

	for a in xrange(0,2):
		test_pair.append(''.join(list(possible_mapping[index] for index in anagram_pair[a])))

	if test_pair[0][0] == "0" or test_pair[1][0] == "0": # leading zeroes are not permitted
		return False,0
	else:
		square_test_0 = int(test_pair[0])
		square_test_1 = int(test_pair[1])
	
	if (square_test_0 in squares_list and square_test_1 in squares_list):
		return True,max(square_test_0,square_test_1)
	else:
		return False,0

def main():
	data  = read_data('p098_words.txt')
	largest_square = 0

	# Get list of anagrams
	anagrams_list = list()
	for i in xrange(0,len(data)-1):
		for j in xrange(i+1,len(data)-1):
			if anagram(data[i],data[j]):
				anagrams_list.append([data[i],data[j]])


	# Obtain unique mapping for each anagram, and check if any mapping yields squares
	for pair in anagrams_list:
		maps = get_mappings(pair[0])
		for possible_map in maps:
			flag, square = is_square_mapping(pair,possible_map)
			if flag == True and square > largest_square:
				largest_square = square
	return largest_square


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # 41.8s