import math
from re import sub
import time
start = time.time()

def read_data(path):

	file = open(path,mode='r').read() #read converts the read object into a string
	# print(str(file))
	words = list(file.replace('"','').split(',')) 
	return words

def sum_value(word):
	letters = list(word)
	sum = 0
	for letter in letters:
		sum += (ord(letter)-64) #ASCII value of A is 65 
	return sum

def triangle_numbers(index):
	result = []
	for n in xrange(1,index): 
		result.append((n*(n+1))/2)
	return result

def main(path):
	result = 0
	elements = read_data(path)

	triangle_num = triangle_numbers(34) # largest english word has numberic count of 540, which corresponds to approx 34 max triangle numbers
	for element in elements:
		word_2_num = sum_value(element)
		if word_2_num in triangle_num:
			result += 1

	return result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main('p042_words.txt'),elapsed)) #2.14576721191e-06 s

 