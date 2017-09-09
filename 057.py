import math 
import time
start = time.time()

'''
def gcd(m,n): #Euclid's method
	while m%n != 0:
		old_m = m
		old_n = n

		m = old_n
		n = old_m%old_n
	return n

class Fraction:
	def __init__ (self, top, bottom):
		self.num = top
		self.den = bottom

	def show(self):
		print(self.num,"/",self.den)

	def __str__ (self):
		return (str(self.num)  + "/" + str(self.den))

	def __mul__(self,other_fraction):
		new_num = self.num*other_fraction.num
		new_den = self.den*other_fraction.den
		return Fraction(new_num,new_den)

	def __add__ (self,other_fraction):
		new_num = self.num*other_fraction.den + self.den*other_fraction.num
		new_den = self.den*other_fraction.den
		# common  = gcd(new_num,new_den)
		# return (Fraction(new_num//common,new_den//common))
		return Fraction(new_num,new_den)


def recursion(n):
	if n == 1:
		return Fraction(1,2)
	return Fraction(2,recursion(n-1))

print(recursion(2)*recursion(1))
print(recursion(3))
'''
def main():
	p = q = 1
	result_count = 0
	for i in xrange(1,1000+1):
		a1,b1 = p + 2*q , p+q
		# print(a1,b1)
		if len(str(a1)) > len(str(b1)):
			result_count += 1
		p,q = a1,b1
	return result_count

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #0.0s


