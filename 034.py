import time
start = time.time()

def extract_digits(n):
	digits = [n%10]
	while n//10 != 0 :
		n = n//10
		digits.append(n%10)
	return digits

def factorial(n):
	if n == 0:
		return 1
	if n==1:
		return n
	else:
		return n*factorial(n-1)

def sum_digits_factorial(n):
	sum_digits = 0
	for digit in extract_digits(n):
		if factorial(digit)>n: #pre-case already
			return 0
		sum_digits +=  factorial(digit)

	return sum_digits

def main():
	result = []
	for i in range(1000000):
		if sum_digits_factorial(i)==i:
			result.append(i)
	return (sum(result)-3)

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) 
