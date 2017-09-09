 # Area A = [ x1(y2 - y3) + x2(y3 - y1) + x3(y1-y2)]/2
from __future__ import division
import math
import time
start = time.time()

def read_data(path):
	file = open(path,mode='r').read() #read converts the read object into a string
	#print(file)
	result =  filter(None,list(file.split('\n'))) #Filter: Removing any null entries
	result =  list(map(int,entry.split(',')) for entry in result)
	return result

def area_triangle(x1,y1,x2,y2,x3,y3):
	return abs(((x1*(y2 - y3)) + (x2*(y3 - y1)) + (x3*(y1-y2)))/2)

def is_inside(points): # Possible approach 1
	area_ABC = area_triangle(points[0],points[1],points[2],points[3],points[4],points[5])
	area_PAB = area_triangle(0,0,points[2],points[3],points[4],points[5])
	area_PBC = area_triangle(points[0],points[1],0,0,points[4],points[5])
	area_PAC = area_triangle(points[0],points[1],points[2],points[3],0,0)
	return (area_ABC == area_PAC + area_PBC + area_PAB)




def main():
	count_result = 0
	data = read_data('p102_triangles.txt')
	for entry in data:
		if is_inside(entry):
			count_result += 1
	return count_result


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #0.0s 