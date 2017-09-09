import time
import math
start = time.time()

#Extremely slow 
def extract_digits(n):
    return list(int(digit) for digit in str(n))

def unique_digits(n):
    return (len(n) == len(set(n)))

def is_pandigital(number):
    digits = extract_digits(number)
    if 0 in digits:
        return False
    if unique_digits(digits) and len(digits)==9:
        return True
    else:
        return False

def main():
    a, b = 0, 1
    for k in xrange(1,500000):        
        first_part  = int(str(b)[:9])
        second_part = int(str(b)[-9:])
        if is_pandigital(first_part) and is_pandigital(second_part):
            return b,k

        a, b, = b, a + b
        print(k)

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) # ~3 hours