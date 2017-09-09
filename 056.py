import time
import math
start = time.time()

#Brute Force method
def sum_digits(n):
	number = [int(i) for i in  str(n)]
	return sum(number)

def main():

	max_digital_sum = 0
	for a in xrange(2,100):
		for b in xrange(2,100):
			# print("a is {} | b is {}".format(a,b))
			sum_digits_number = sum_digits(a**b)
			if sum_digits_number > max_digital_sum:
				# print(number)
				# print("Digit Sum {}".format(sum_digits_number))
				max_digital_sum = sum_digits_number

	return max_digital_sum

elapsed = time.time() - start 
print ("%s found in %s seconds" % (main(),elapsed)) #0.3s

