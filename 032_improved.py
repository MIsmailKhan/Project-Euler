import math
import time

start = time.time()

# fairly verbose solution

def extract_digits(n):
	digits = [n%10]
	while n//10 != 0 :
		n = n//10
		digits.append(n%10)
	return digits

def factors(n):
	result = []
	for i in range(2,(n//2)+1):

		if i in result:
			break

		if n%i == 0:
			result.extend((i,(n/i)))

	# result = list(set(result))
	return result

def unique_digits(n):
	return (len(n) == len(set(n)))

def is_pandigital(number):
	digits = extract_digits(number)
	if 0 in digits:
		return False
	if unique_digits(digits) and len(digits)==9:
		return True
	else:
		return False

def main():
	solution = 0
	for num in range(4000,8000):
		
		factor_number = factors(num)
		for i in xrange(0,len(factor_number),2):
			feed = str(num) + str(factor_number[i]) + str(factor_number[i+1])
			# print(feed)
			if is_pandigital(int(feed)):
				print(num)
				solution += num	
				break
	return solution
	

'''
(4396, 28, 157)
(5346, 18, 297)
(5796, 12, 483)
(6952, 4, 1738)
(7254, 39, 186)
(7632, 48, 159)
(7852, 4, 1963)
'''

print(is_pandigital(439628157))
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) 
