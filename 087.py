import math
import time
start = time.time()

def is_prime(n):
    # n = abs(n)
    if n<=1: 
        return False
    for i in range(2,(int(math.sqrt(n))+1)):
        if n%i == 0:
            return False
            break
    return True

limit = 50000000
prime_list = [2]
for i in xrange(3,int(math.sqrt(limit)),2):
	if is_prime(i):
		prime_list.append(i)

def main():
    count = set()
    for i in prime_list:
        for j in prime_list:
            for k in prime_list:
                test = i**2 + j**3 + k**4
                if test >= limit: break
                count.add(test)
                     
    return len(count)


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))

