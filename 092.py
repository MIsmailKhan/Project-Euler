import math 
import time
start = time.time()

def extract_digits(n):
	return list(int(digit) for digit in str(n))

def square_digit(digits_list):
	return sum(entry**2 for entry in digits_list)

def main():
	count_result = 0 
	dict_results = {1:False}

	for n in xrange(2,567+1): # 9,999,999 has square digit sum of 567
		number = n
		flag = False

		while number != 1 and number != 89:
			number = square_digit(extract_digits(number))

		if number == 89:
			count_result += 1
			flag = True

		dict_results[n] = flag
	
	for i in xrange(568,10000000):
		number_2 = square_digit(extract_digits(i))
		count_result += 1 if dict_results[number_2] == True else 0
		
	return count_result
			
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #33.6s
