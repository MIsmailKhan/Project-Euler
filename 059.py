import math
import time 
start = time.time()

def read_data(path):

	file = open(path,mode='r').read() #read converts the read object into a string
	# print(str(file))
	data = list(file.split(',')) 
	data = map(int,data)
	return data


def main():
	cipher = read_data('p059_cipher.txt')
	decrypt = []
	test = []
	ascii_values = map(lambda x: chr(x), cipher)
	for key in xrange(291,367):
		for value_0 in cipher:
			decrypt.append(int(bin(value_0) ^ bin(key))
		for value_1 in decrypt:
			test = 


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))