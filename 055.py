#lychrel number 
import time
import math
start = time.time()

def palindrome(n):
	return int(str(n)[::-1])

def is_palindrome(n):
	return (n == int(str(n)[::-1]))

def is_lychrel(n):
	number_iterations = 0
	num = n + palindrome(n) # to take into case palindromic numbers also 
	while(not is_palindrome(num) and number_iterations <= 50):
		# print(num)
		number_iterations += 1
		num = num + palindrome(num)
	if number_iterations < 50:
		return False
	else:
		return True

def main():
	result_count = 0
	for i in xrange(1,10001):
		if is_lychrel(i):
			result_count += 1
	return result_count

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #0.1s