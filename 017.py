#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

import time
import numpy as np 
import math

start = time.time()

# Static lists for purpose of illustration
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100,1000]
letters = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred","thousand"]

key_dict = {}
for i in range(len(numbers)):
	key_dict[numbers[i]] = letters[i]

def units(i):
	#print (key_dict[i])
	return len(key_dict[i])

def tenth(j):
	if j < 21:
		return units(j) 
	else:
		return (units((j//10)*10) + units(j%10)) #first part:summing letters of tenth place

# note that (int(j/10) returns the same as j//10 | //-floordiv operation

def hundreth(k):
	if (k%100)==0:
		return ((units(k//100) + units(100)) + tenth(k%100)) #in brackets: summing letters of hundreds place
	else:
		return ((units(k//100) + units(100)) + tenth(k%100) + 3) #in brackets: summing letters of hundreds place

def thousanth(l):
	return ((units(l//1000) + units(1000))) # + hundreth(l%100)) #in brackets: summing letters of thousanth place


total_letters = 0 

for number in range(1,1001):
	
	if number <= 20: 
		total_letters += units(number)
	elif (20 < number < 100):
		total_letters += tenth(number)
	elif 100 <= number < 1000:
		total_letters += hundreth(number)
	elif number >= 1000:
		total_letters += thousanth(number)
	else:
		print("Number invalid")
	#print(number)
	#print 

elapsed = time.time() - start
print "%s found in %s seconds" % (total_letters,elapsed) #answer is 21122
