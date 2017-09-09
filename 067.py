import math
import time
start = time.time()

#Using bottom-up approach

def read_data(path):

	file = open(path,mode='r').read() #read converts the read object into a string
	#print(file)
	result =  filter(None,list(file.split('\n'))) #Filter: Removing any null entries
	result =  list(map(int,entry.split(' ')) for entry in result)
	return result

def main():
	triangle = read_data('p067_triangle.txt')

	last_row_index = len(triangle)-1
	for row in xrange(last_row_index,0,-1):
		for column in xrange(0,row):
			triangle[row-1][column] += max(triangle[row][column],triangle[row][column+1])
	return triangle[0][0]
	
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #0.0s or 9.53674316406e-07 s
