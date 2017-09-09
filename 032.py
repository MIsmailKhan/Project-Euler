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

def is_pandigital(number,product_1,product_2):
	digits = [x for x in range(1,10)]

	digits_number = extract_digits(number)
	digits_product_1 = extract_digits(product_1)
	digits_product_2 = extract_digits(product_2)

	if (0 in digits_number) or (0 in digits_product_1) or (0 in digits_product_2):
		return False
	
	if (unique_digits(i) for i in zip(digits_number,digits_product_1,digits_product_2)): #checking if inputs have unique digits

		if len(set(digits_number)^set(digits_product_1)^set(digits_product_2)) == (len(digits_number)+len(digits_product_2)+len(digits_product_1)):
			digits = list(set(digits)^set(digits_number)^set(digits_product_1)^set(digits_product_2))
		else:
			return False
	else:
		return False

	if len(digits) == 0:
		return True

solution = 0
for num in range(10000):
	factor_number = factors(num)
	for i in xrange(0,len(factor_number),2):
		if is_pandigital(num,factor_number[i],factor_number[i+1]):
			print(num,factor_number[i],factor_number[i+1])
			solution += num
			break
	
elapsed = time.time() - start
print ("%s found in %s seconds" % (solution,elapsed)) 
