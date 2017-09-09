import math
import time
start = time.time()

def read_data(path):

	file = open(path,mode='r').read() #read converts the read object into a string
	#print(file)
	result =  filter(None,list(file.split('\n'))) #Filter: Removing any null entries
	result =  list(map(int,entry.split(' ')) for entry in result)
	return result

def main():
	triangle = read_data('018.txt')

	last_row_index = len(triangle)-1
	for row in xrange(last_row_index,0,-1):
		for column in xrange(0,row):
			triangle[row-1][column] += max(triangle[row][column],triangle[row][column+1])
			# print(rows[index+1])
	return triangle[0][0]
	
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))
