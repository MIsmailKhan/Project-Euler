import time 
start = time.time()

def is_palindrome(a):
	palindrome = a[::-1]
	return (palindrome == a)

def main():
	total_sum = 0
	for i in xrange(1,1000000):
		binary = str(bin(i))[2:] 
		if is_palindrome(binary) and is_palindrome(str(i)):
			total_sum += i
	return total_sum

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #9.53674316406e-07 s

