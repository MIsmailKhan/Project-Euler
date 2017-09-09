import time 
start =time.time()

def champernowne_constant(n):
	result = ""
	for i in range(1,n):
		result = result + str(i)		
	return result

def return_value(string,index):
	return int(string[index-1])

def main():
	constant = champernowne_constant(10**6)
	result = 1
	for num in xrange(0,7):
		result = result * return_value(constant,10**num) 
	return result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))


