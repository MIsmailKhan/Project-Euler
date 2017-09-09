from copy import copy, deepcopy

import math
import time 
start = time.time()

#Flawed algorithm

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
	data_matrix = read_data('test_matrix.txt')  # p082_matrix.txt
	matrix_dim = len(data_matrix)
	sum_matrix = deepcopy(data_matrix) 
	
	for i in xrange(matrix_dim-1,-1,-1):
		for j in xrange(matrix_dim):

			if j == 0: continue # starting pt: 0th column
			elif j == matrix_dim: sum_matrix[i][j] +=  sum_matrix[i][j-1] # Last column
			elif i == matrix_dim: sum_matrix[i][j] += sum_matrix[i][j-1] # Case for last row
			elif i == 0 : sum_matrix[i][j] += min(sum_matrix[i+1][j],sum_matrix[i][j-1]) # Case for first row
			else : 
				sum_matrix[i][j] += min(sum_matrix[i-1][j],sum_matrix[i][j-1])  # All other cases 

	print(sum_matrix)
	# Returning the minimal sum path
	sum_minimal_path_global = 99999999
	

	last_column_entries = []
	for x in xrange(matrix_dim-1,0,-1):
		last_column_entries.append(sum_matrix[x][matrix_dim-1])
	print(last_column_entries)

	for index_row,last_column_entry in enumerate(last_column_entries):

		column = matrix_dim - 1
		row = (matrix_dim-1) - index_row

		print("Checking with {} entry in last column".format(last_column_entry))
		sum_minimal_path = last_column_entry + sum_matrix[index_row][column-1]
		column -= 1

		while(column != 0):
			print("Start: {}".format(sum_matrix[row][column]))
			print(row,column,matrix_dim-1)

			if row == (matrix_dim - 1):
				to_take = min(sum_matrix[row][column-1],sum_matrix[row-1][column]) # Case for last row
				print("Case 1")
			elif row == 0:
				to_take = min(sum_matrix[row][column-1],sum_matrix[row+1][column]) # Case for first row
				print("Case 2")
			else:
				to_take = min(sum_matrix[row][column-1],sum_matrix[row-1][column],sum_matrix[row+1][column]) # remaining entries
				print("Case 3")

			print("to_take {}".format(to_take))

			if to_take == sum_matrix[row][column-1]:
				sum_minimal_path += data_matrix[row][column-1]
				column -= 1
			elif to_take == sum_matrix[row-1][column]:
				sum_minimal_path += data_matrix[row-1][column]
				row -= 1
			else:
				sum_minimal_path += data_matrix[row+1][column]
				row += 1

		if sum_minimal_path < sum_minimal_path_global:
			sum_minimal_path_global = sum_minimal_path


	return sum_minimal_path_global


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # 0.0s
