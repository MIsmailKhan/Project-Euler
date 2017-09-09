import math 
import time
import itertools
start = time.time()

 # Inefficient and highly specific solution
 # Need to improve solution
 
def read_data(path):

	file = open(path,mode='r').read() #read converts the read object into a string
	result =  filter(None,list(file.split('\n'))) # Filter: Removing any null entries
	return result

def extract_digits(n):
	return list(int(digit) for digit in str(n)) 

def permutations_n(n):
	num = str(n)
	permutes = list(''.join(i) for i in itertools.permutations(num))
	return permutes

def main():
	result = 0
	data = read_data('p079_keylog.txt')
	
	set_digits = set()
	for entry in data:
		for digit in extract_digits(entry):
			set_digits.add(digit)             # Smallest number that satisfies the set will be the one where there is only one of each code digit in the number

	num = ''
	num = num.join(str(entry) for entry in set_digits)
	possibilities = permutations_n(num)

	for possibility in possibilities:
		flag = True
		for code in data:
			if possibility.index(code[0]) < possibility.index(code[1]) and possibility.index(code[1]) < possibility.index(code[2]):
				continue
			else:
				flag = False

		if flag == True:
			return possibility


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))