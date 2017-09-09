import time
import math
from itertools import permutations
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

prime_list = [2]
for i in xrange(3,10000,2):
	if is_prime(i):
		prime_list.append(i)

def checking(l):
	flag = True
	possibilities = map(int,[''.join(i) for i in permutations(l,2)])
	for entry in possibilities:
		if is_prime(entry):
			continue
		else:
			flag = False
			break

	return flag

def main():
	result = []
	for index_1,a in enumerate(prime_list):

		for index_2,b in enumerate(prime_list[index_1+1:]):
			if checking([str(a),str(b)]):

				for index_3,c in enumerate(prime_list[index_2+1:]):
					if checking([str(a),str(b),str(c)]):

						for index_4,d in enumerate(prime_list[index_3+1:]):
							if checking([str(a),str(b),str(c),str(d)]):

								for e in prime_list[index_4+1:]:
									if checking([str(a),str(b),str(c),str(d),str(e)]):
										result.extend((a,b,c,d,e))
										return sum(result)

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #98.3s
