import time
import math
import itertools 

start = time.time()

def is_prime(n):
	# n = abs(n)
	for i in range(2,(int(math.sqrt(n))+1)):
		if n%i == 0:
			return False
			break
	return True

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def rotations(n):
    answer = []
    rotation = str(n)z
    while not rotation in answer:
        answer.append(rotation)
        rotation = (str(rotation)[1:] + str(rotation)[0])
    answer = map(int, answer)
    return answer

def main():
	count = 0
	for i in range(2,1000001): #Brute method | Improve_1:replace range() with sieve_of_primes_to()
		flag = True
		get_circulars = rotations(i)
		for element in get_circulars:
			if is_prime(element):
				pass
			else:
				flag = False
				break
		if flag is True:
			count += 1
	return count

# Brute: 2.14576721191e-06 s
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) 






