from copy import copy, deepcopy

import math
import time 
start = time.time()

def read_data(path):

	file = open(path,mode='r').read() #read converts the read object into a string
	# print(str(file))
	data = filter(None,list(file.split('\n')))
	matrix = [[]]
	for index,entry in enumerate(data):
		entry.replace(" ","")
		matrix.append(map(int,list(entry.split(','))))
	return filter(None,matrix)

def main():
	data_matrix = read_data('p081_matrix.txt')  # test_matrix.txt
	matrix_dim = len(data_matrix)
	sum_matrix = deepcopy(data_matrix) 
	
	for i in xrange(matrix_dim):
		for j in xrange(matrix_dim):

			if i == 0 and j == 0: continue # [0,0] case
			elif i == 0 : sum_matrix[i][j] += sum_matrix[i][j-1] # Case for first row
			elif j == 0 : sum_matrix[i][j] += sum_matrix[i-1][j] # #Case for first column
			else : 
				sum_matrix[i][j] += min(sum_matrix[i-1][j],sum_matrix[i][j-1])  # All other cases 

	# Returning the minimal sum path
	sum_minimal_path = data_matrix[-1][-1]
	row = column = matrix_dim - 1 
	while(row != 0 or column != 0):
		to_take = min(sum_matrix[row][column-1],sum_matrix[row-1][column])

		if to_take == sum_matrix[row][column-1]:
			sum_minimal_path += data_matrix[row][column-1]
			column -= 1
		else:
			sum_minimal_path += data_matrix[row-1][column]
			row -= 1

	return sum_minimal_path


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # 0.0s
