import math
import time

start = time.time()

def extract_digits(n):
	digits = [n%10]
	while n//10 != 0 :
		n = n//10
		digits.append(n%10)
	return digits

def sum_fifth_power(digits):
	sum = 0
	for digit in digits:
		sum += digit**5
	return sum

def check_equal(number,sum):
	if number == sum:
		return True 
	else:
		return False

def main(n):
	solution = 0 
	for number in xrange(10,((9**5)*(n-1))):
		if check_equal(number,sum_fifth_power(extract_digits(number))):
			solution += number
	return solution

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(5),elapsed)) 
