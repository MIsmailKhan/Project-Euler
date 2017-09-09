import math 
import time
start = time.time()

def read_data(path):

	file = open(path,mode='r').read() #read converts the read object into a string
	result =  filter(None,list(file.split('\n'))) #Filter: Removing any null entries
	return result

def main():
	greatest_value = 0
	line_number_result = 0
	data = read_data('p099_base_exp.txt')
	for line,entry in enumerate(data):
		base, exponent = map(int,entry.split(','))
		test = exponent * math.log(base)
		if test > greatest_value:
			greatest_value = test
			line_number_result = line + 1

	return line_number_result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))