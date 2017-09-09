import time
import math
import operator as op
start = time.time()

# http://www.mathblog.dk/project-euler-113-googol-not-bouncy/

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

def main():
	return ncr(100+10,10) + ncr(100+9,9) - (10 * 100) -2


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) 