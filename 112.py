from __future__ import division
import math
import time
start = time.time()

def extract_digits(n):
	return list(int(digit) for digit in str(n))

def is_increasing(n):
	digits_n = extract_digits(n)
	flag = True
	for i in xrange(0,len(digits_n)-1):
		if digits_n[i] <= digits_n[i+1]:
			pass
		else:
			return False
	return True

def is_decreasing(n):
	digits_n = extract_digits(n)
	for i in xrange(0,len(digits_n)-1):
		if digits_n[i] >= digits_n[i+1]:
			pass
		else:
			return False
	return True

def is_bouncy(n):
	flag1 = is_increasing(n)
	flag2 = is_decreasing(n)
	return (not flag1 and not flag2)

def main():
	i = 0
	t = 0
	bouncy = []
	while(t<0.99):
		i += 1
		if is_bouncy(i):
			bouncy.append(i)
		t = len(bouncy)/i
		# print(i,t)

	return i 

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #9.2s