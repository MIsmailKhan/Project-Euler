import time
import math
start = time.time()

# Farily Brute Force Solution

def gcd(m, n):
	while m % n != 0:
		old_m = m
		old_n = n

		m = old_n
		n = old_m % old_n
	return n

class Fraction():

	def __init__(self,top,bottom):

		if type(top) != int or type(bottom) != int: 
			raise ValueError('inputs must be integers')
		self.num = top 
		self.den = bottom 

	def __str__(self):
		return (str(self.num) + "/" + str(self.den))

	def __repr__(self):
		return 'Fraction({0.num}, {0.den})'.format(self) 
		

	def show(self):
		print(self.num,"/",self.den)

	
	def __add__(self,other):
		new_num = self.num*other.den + other.num*self.den
		new_den = self.den*other.den
		return Fraction(new_num,new_den)

	def __radd__(self,other): 
		try:
			return self.__add__(other)
		except:
			return (other).__add__(self)

	def __iadd__(self,other): 
		self = self.__add__(other)
		return self

	def __sub__(self,other): 
		new_num = self.num*other.den - other.num*self.den
		new_den = self.den*other.den
		return Fraction(new_num,new_den)

	def __mul__(self,other): 
		new_num = self.num * other.num
		new_den = self.den * other.den
		return Fraction(new_num,new_den)

	def __truediv__(self,other): 
		new_num = self.num * other.den
		new_den = self.den * other.num
		return Fraction(new_num,new_den)

	def __eq__(self, other):
		first_num = self.num * other.den
		second_num = other.num * self.den

		return first_num == second_num

	def __gt__(self,other):
		new_num_self = self.num * other.den
		new_num_other = other.num * self.den
		return (new_num_self > new_num_other)

	def __ge__(self,other): 
		return self.__gt__(other) or self.__eq__(other)

	def __lt__(self,other): 
		new_num_self = self.num*other.den
		new_num_other = other.num*self.den
		return (new_num_self < new_num_other)

	def __le__(self,other): 
		new_num_self = self.num*other.den
		new_num_other = other.num*self.den
		return self.__lt__(other) or self.__eq__(other)

	def __ne__(self,other): 
		return not self.__eq__(other)

	def get_num(self): 
		return self.num

	def get_den(self):
		return self.den

	def reduced_fraction(self):
		common = gcd(self.num,self.den)
		return (self.num//common == self.num)



def main():
	list_fractions = []
	begin_range = Fraction(1,3)
	end_range = Fraction(1,2)
	for d in xrange(2,12000+1):
		print(d)
		for n in xrange(int(0.32*d),int(0.51*d)+1):
			test_fraction = Fraction(n,d)
			if (test_fraction.reduced_fraction()) and (test_fraction < end_range) and (test_fraction > begin_range):
					list_fractions.append(test_fraction)

	return len(list_fractions)

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #30.2 s