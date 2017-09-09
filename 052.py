import time
import math

start = time.time()

 # Brute Force Method
def extract_digits(n):
	return [int(i) for i in str(n)]

def main():
	num = 1
	found_result = False
	while(found_result == False):
		# print("Number is %d"%num)
		digits = set(extract_digits(num))
		for a in xrange(2,7):
			result = a*num
			digits_num = set(extract_digits(result))
			# print(digits,digits_num)
			if digits_num == digits:
				if a == 6:
					found_result =  True
				continue
			else:
				break
		num += 1
	return (num-1)

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))

