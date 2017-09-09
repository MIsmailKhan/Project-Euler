import math 
import time
start = time.time()

# http://people.revoledu.com/kardi/tutorial/ContinuedFraction/Decimal-Fraction-Conversion.htm
# Solution returning incorrect values after n = 21, need to investigate

def main(convergent):
	number = math.exp(1)
	a = a0 = int(number)
	r = r0 = number - float(a0)
	y = y0 = 1/r0

	p_prev = 1
	q_prev = 0

	p_current = a0
	q_current = 1

	n = 1
	while(n <= convergent):
		a = int(y)
		r = y - a
		y = 1/r

		p_next = a*p_current + p_prev
		q_next = a*q_current + q_prev

		p_prev = p_current
		q_prev = q_current

		p_current = p_next
		q_current = q_next

		n += 1

	digits  = list(int(digit) for digit in str(p_prev))
	return sum(digits)

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(100),elapsed))

'''
Solution
n0, n1, L = 1, 2, 100

for i in xrange(2, L+1): 
    n0, n1 = n1, n0 + n1 * (1 if i % 3 else 2 * i//3)
    print(i,sum(map(int, str(n1))))

print "Project Euler 65 Solution =", sum(map(int, str(n1)))