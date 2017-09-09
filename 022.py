import math
from re import sub
import time
start = time.time()

def read_data(path):

	file = open(path,mode='r').read() #read converts the read object into a string
	# print(str(file))
	words = list(file.replace('"','').split(',')) 
	return words

def sort_list(data):
	return sorted(data)

def sum_value(word):
	letters = list(word)
	sum = 0
	for letter in letters:
		sum += (ord(letter)-64) #ASCII value of A is 65 
	return sum

def main(path):
	answer = 0
	elements = sort_list(read_data('names.txt'))
	for i, element in enumerate(elements):
		answer += (sum_value(element) * (i+1))
	return answer

	
elapsed = time.time() - start
print ("%s found in %s seconds" % (main('names.txt'),elapsed)) 
