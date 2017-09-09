import math
import time
start = time.time()

# Fairly verbose solution 
# Can create function to reduce length of program (repetitive commands)

def read_data(path):

	file = open(path,mode='r').read() #read converts the read object into a string
	result =  filter(None,list(file.split('\n'))) #Filter: Removing any null entries
	return result

roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} 
	
def roman_numeral_value(string_numeral):
	value = 0
	for index in xrange(0,len(string_numeral)-1):

		letter_value = roman_dict[string_numeral[index]]
		next_letter_value = roman_dict[string_numeral[index+1]]

		if letter_value < next_letter_value:
			value -= letter_value
		else:
			value += letter_value

	value += roman_dict[string_numeral[-1]]

	return value

def minimal_form(number):

	difference = number
	no_of_characters = 0 
	roman_numeral = []

	while difference != 0:

		if difference//1000 >= 1:
			no_of_characters += difference//1000 #Adding M's
			roman_numeral.append("M"*(difference//1000))
			difference -= (difference//1000)*1000
		elif difference//500 >= 1:
			if difference >= 900:
				no_of_characters += 2 # CM is representation of 900
				roman_numeral.append("CM")
				difference -= 900
			else:
				no_of_characters += difference//500 #Adding D's
				roman_numeral.append("D"*(difference//500))
				difference -= (difference//500)*500
		elif difference//100 >= 1:
			if difference >= 400:
				no_of_characters += 2 # CD is representation of 400
				roman_numeral.append("CD")
				difference -= 400
			else:
				no_of_characters += difference//100 #Adding C's
				roman_numeral.append("C"*(difference//100))
				difference -= (difference//100)*100
		elif difference//50 >= 1:
			if difference >= 90:
				no_of_characters += 2 # XC is representation of 90
				roman_numeral.append("XC")
				difference -= 90	
			else:
				no_of_characters += difference//50 #Adding L's
				roman_numeral.append("L"*(difference//50))
				difference -= (difference//50)*50
		elif difference//10 >= 1:
			if difference >= 40:
				no_of_characters += 2 # XL is representation of 40
				roman_numeral.append("XL")
				difference -= 40	
			else:
				no_of_characters += difference//10 #Adding X's
				roman_numeral.append("X"*(difference//10))
				difference -= (difference//10)*10
		elif difference//5 >= 1:
			if difference == 9:
				no_of_characters += 2 # IX is representation of 9
				roman_numeral.append("IX")
				difference -= 9
			else:
				no_of_characters += difference//5 #Adding V's
				roman_numeral.append("V"*(difference//5))
				difference -= (difference//5)*5			
		else:
			if difference == 4:
				no_of_characters += 2 # IV is representation of 4
				roman_numeral.append("IV"*(difference//5))
				difference -= 4
			else:
				no_of_characters += difference
				roman_numeral.append("I"*difference)
				difference -= difference

	return no_of_characters

def main():
	characters_saved = 0 
	roman_data = read_data('p089_roman.txt')
	for entry in roman_data:
		if len(entry) > minimal_form(roman_numeral_value(entry)):
			characters_saved += len(entry) - minimal_form(roman_numeral_value(entry))

	return characters_saved


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) #0.1s 
