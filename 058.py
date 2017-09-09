from __future__ import division
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

def main():
    count_prime = 0

    ratio = 1.0
    n = 3
    index = 1
    iterator = 2
    while(ratio > 0.1):
        if is_prime(n):
            count_prime += 1
        if index%4 == 0:
            iterator += 2
        ratio = count_prime/(index+1)

        index += 1
        n += iterator

    return math.sqrt(n) #Returns length of side

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #8.4s



