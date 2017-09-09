import time
start=time.time()

def extract_digits(n):
	return list(int(digit) for digit in str(n)) 

dict_factorials = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def sum_digits_factorial(n):
	sum_digits = 0
	for digit in extract_digits(n):
		sum_digits +=  dict_factorials[digit]

	return sum_digits

def repeated_length(n):
	loop = [n]
	while(len(loop) == len(set(loop))):
		loop.append(sum_digits_factorial(loop[-1]))

	return len(loop) - 1


def main():
	count_result =0
	for i in xrange(10,1000000):
		print
		if repeated_length(i) == 60:
			count_result += 1
	return count_result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # 94.4s
