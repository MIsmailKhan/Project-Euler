from __future__ import division
import math
import time

# fairly Brute force solution
# fairly verbose solution

start = time.time()

def extract_digits(n):
	digits = [n%10]
	while n//10 != 0 :
		n = n//10
		digits.append(n%10)
	return digits

def common_digit(a,b):
	common_digit = list(set(extract_digits(a)).intersection(set(extract_digits(b))))
	if len(common_digit) > 0:
		if (0 in common_digit):
			return 99 #wrong
		else:
			return common_digit[0]
	else:
		return 99 #wrong

def main():
	result = []
	for a in xrange(10,100):
		for b in xrange(10,a):
			test = common_digit(a,b)
			if test == 99:
				#print("None: {},{}".format(a,b))
				continue
			else:
				#print("Yes: {},{}".format(a,b))
				digits_a = extract_digits(a)
				digits_b = extract_digits(b)
				# print(digits_a,digits_b)
				digits_a.remove(test)
				digits_b.remove(test)
				# print (digits_a,digits_b)
				if digits_a[0]==0 or digits_b[0]==0: # checking for trivial values
					continue
				if (digits_b[0]/digits_a[0]) == (b/a) :
					result.append([b,a])
	return result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) 