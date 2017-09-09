import time
import math

#Faulty program , needs revision
start = time.time()

def is_prime(n):
	# n = abs(n)
	if n<=0 or n==1: #tweak only for this code, mathematically unsound
		return False
	for i in range(2,(int(math.sqrt(n))+1)):
		if n%i == 0:
			return False
			break
	return True


#Generate squares list
squares = []
for i in xrange(1,100):
	squares.append(i*i)

def check_square(n):
	print("Check squares {}".format(n))
	print(squares)
	if n in squares:
		return True
	else:
		return False

def check_eqn(odd_composite,prime):
	eqn = int((odd_composite - prime)/2) 
	print eqn
	if check_square(eqn): #complies with Goldbach Conjecture
		return True 
	else:
		return False 


def main():

	numbers = list(range(3,10000,2)) #1 is neither prime nor composite, iterate in steps of 2 since primes after 2 are odd and we are only to use odd composites
	primes = [2]
	odd_composites = []
	for number in numbers:
		if is_prime(number):
			primes.append(number)
		else:
			odd_composites.append(number)

	for i,composite in enumerate(odd_composites): 
		for prime_num in primes[:i+1]:
			print composite, prime_num
			if not check_eqn(composite,prime_num): #check for first number that does not fit equation
				print prime_num,composite
				return composite

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))


'''
while True:
 if is_prime(number):
  primes.append(number)
 else:
  for i in primes:
   if math.sqrt(((number-i)/2)) == int(math.sqrt(((number-i)/2))):
    break
  else:
   print number
   break
'''