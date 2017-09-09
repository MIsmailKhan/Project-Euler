import math 
import time
start = time.time()

# Using right angle triangles concept P39

def right_angle(side_1,side_2,side_3):
	if ((side_1)**2 + (side_2)**2) == (side_3)**2:
		return True
	else:
		return False

def main():
	count_result = 0
	for p in xrange(12,1500000+1,2): # can't have an odd perimeter
		print(p)
		no_of_solutions = 0
		flag = True

		for a in xrange(2,int(p/3.4142)+1):
			if no_of_solutions > 1:
				flag = False
				break

			if p*(p - 2*a) % (2*(p - a)) == 0: 
				no_of_solutions += 1

		if flag == True:
			count_result += 1

	return count_result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))