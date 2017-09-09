import time
import math
start = time.time()

# https://en.wikipedia.org/wiki/Euler%27s_totient_function
# Solution derived from definition of totient function

def is_prime(n):
    # n = abs(n)
    if n<=1: 
        return False
    for i in range(2,(int(math.sqrt(n))+1)):
        if n%i == 0:
            return False
            break
    return True

prime_list = [2]
for i in xrange(3,200,2):
	if is_prime(i):
		prime_list.append(i)


def main():
    limit = 1000000
    result = 1
    index  = 0
    while (result*prime_list[index]) < limit:
        result *= prime_list[index]
        index += 1
    return result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))