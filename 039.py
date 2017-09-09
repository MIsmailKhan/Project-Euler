import math 
import time
start = time.time()

def right_angle(side_1,side_2,side_3):
	if ((side_1)**2 + (side_2)**2) == (side_3)**2:
		return True
	else:
		return False

def main():
	max_solutions = 0
	result = 0
	for p in xrange(2,1002,2):
		no_of_solutions = 0
		for a in xrange(2,int(p/3.4142)+1):
			if p*(p - 2*a) % (2*(p - a)) == 0: 
				no_of_solutions += 1
				# print(p,no_of_solutions)
				if no_of_solutions>=max_solutions: 
					print(p)
					max_solutions = no_of_solutions
					result = p
		
	return max_solutions,result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # 0.0s