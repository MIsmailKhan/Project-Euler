import time
import math
start = time.time()

def main():
	digits = ['1','2','3','4','5','6','7','8','9','0']
	for i in xrange(pow(10,9),pow(10,10),10): # Since last digit of the square is a 0 , the square root must be a multiple of 10
		num = str(i**2)
		flag = True
		for position in xrange(0,19-1,2):
			if num[position] == digits[position//2]:
				pass
			else:
				flag = False
				break

		if flag == True:
			return i

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # 24.5s
