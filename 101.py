from __future__ import division
import math
import time
import itertools
start = time.time()

# http://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html
# Interpolation : Project Nayuki

def gcd(m, n):
	while m % n != 0:
		old_m = m
		old_n = n

		m = old_n
		n = old_m % old_n
	return n

class Fraction():

	def __init__(self,top,bottom):

		if type(top) != int or type(bottom) != int: # Programming exercise Q5
			raise ValueError('inputs must be integers')

		common = gcd(abs(top),abs(bottom)) # Programming exercise Q2 , adding abs : Programming exercise Q3
		self.num = top//common
		self.den = bottom//common

	def __str__(self):
		return (str(self.num) + "/" + str(self.den))

	# Programming exercise Q9: Note that __str__ is called by default unless not there.
	# __repr__ :Return a string containing a printable representation of an object. 
	# For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(),
	# otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional
	# information often including the name and address of the object.
	# A class can control what this function returns for its instances by defining a __repr__() method.

	def __repr__(self):
		return 'Fraction({0.num}, {0.den})'.format(self) # Better implementation
		# return ("Fraction(" + str(self.num) + str(self.den) + ")") # Initaial solution

	def show(self):
		print(self.num,"/",self.den)

	
	def __add__(self,other):
		new_num = self.num*other.den + other.num*self.den
		new_den = self.den*other.den
		# common = gcd(new_num,new_den)
		return Fraction(new_num,new_den)

	def __radd__(self,other): #Reflective addition, called when __add__ fails. It is possible that the operation is reflective and hence __radd__ is called upon
	#One scenario is when the denominator isn't defined or we are adding a fraction with an integer
		try:
			return self.__add__(other)
		except:
			return (other).__add__(self)

	def __iadd__(self,other):  # Programming exercise Q8: a = iadd(a, b) is equivalent to a += b. 
		self = self.__add__(other)
		return self

	def __sub__(self,other): # Programming exercise Q3
		new_num = self.num*other.den - other.num*self.den
		new_den = self.den*other.den
		return Fraction(new_num,new_den)

	def __mul__(self,other): # Programming exercise Q3
		new_num = self.num * other.num
		new_den = self.den * other.den
		return Fraction(new_num,new_den)

	def __truediv__(self,other): # Programming exercise Q3
		new_num = self.num * other.den
		new_den = self.den * other.num
		return Fraction(new_num,new_den)

	def __eq__(self, other):
		first_num = self.num * other.den
		second_num = other.num * self.den

		return first_num == second_num

	def __gt__(self,other): # # Programming exercise Q4
		new_num_self = self.num * other.den
		new_num_other = other.num * self.den
		return (new_num_self > new_num_other)

	def __ge__(self,other): # Programming exercise Q4
		return self.__gt__(other) or self.__eq__(other)

	def __lt__(self,other): # Programming exercise Q4
		new_num_self = self.num*other.den
		new_num_other = other.num*self.den
		return (new_num_self < new_num_other)

	def __le__(self,other): # Programming exercise Q4
		new_num_self = self.num*other.den
		new_num_other = other.num*self.den
		return self.__lt__(other) or self.__eq__(other)

	def __ne__(self,other): # Programming exercise Q4
		return not self.__eq__(other) #Pay attention to implementation

	def get_num(self): # Programming exercise Q1
		return self.num

	def get_den(self): # # Programming exercise Q1
		return self.den

degree = 10

def optimum_polynomial(k,n):
	# Lagrange interpolating polynomial
	sum_result = Fraction(0,1)
	for i in xrange(k+1):
		product = Fraction(generating_function(i),1) #f(xi) or y term
		for j in xrange(1,k+1):
			if j != i:
				product *= Fraction(n - j, i - j) # Lagrange weighting function
		sum_result += product
	return sum_result

def generating_function(n):
	return sum((-n)**i for i in range(degree + 1))

def main():
	ans = Fraction(0,1)
	for k in xrange(1,degree+1):
		for n in itertools.count(k+1):
			if n == degree + 2:
				raise AssertionError()
			reference = Fraction(generating_function(n),1)
			term  = optimum_polynomial(k,n)
			if term != reference:
				ans += term
				break
	return ans

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))