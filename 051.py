import math
import time 
start = time.time()

def is_prime(n):
	# n = abs(n)
	if n<=0 or n==1: 
		return False
	for i in range(2,(int(math.sqrt(n))+1)):
		if n%i == 0:
			return False
			break
	return True

def repeat_digits(n):
    num = str(n)
    digits = set(i for i in num)
    to_check = digits.intersection(set(['0','1','2']))

    for digit in to_check:
        eight_prime = 0

        for i in xrange(0,9+1):
            test = num.replace(digit,str(i))
            if len(str(int(test))) == len(num): #to avoid problem of 0 being in the highest value digits

                if is_prime(int(test)):
                    eight_prime += 1
                    # print(test)
                    
        if eight_prime == 8:
            return True

    return False

prime_list = []
for i in xrange(1,200000):
	if is_prime(i):
		prime_list.append(i)

def main():
    to_iterate = ['0','1','2']
    for entry in prime_list:       
        if any(x in str(entry) for x in to_iterate) and not any(y in str(entry)[-1] for y in to_iterate):
            if repeat_digits(entry):
                return entry
        else:
            continue

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #1.6s
