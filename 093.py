from __future__ import division

import time
import math
import itertools
start = time.time()

# Buggy, does return correct consecutive list length for 1258, but returning higher numbers for others
'''
(('1', '2', '5', '8'), 52, 70)
(('2', '6', '8', '9'), 57, 123)
(('3', '4', '6', '7'), 52, 95)
(('3', '5', '6', '8'), 59, 110)
(('4', '5', '6', '8'), 53, 114)
(('4', '5', '7', '8'), 52, 120)
(('4', '5', '7', '9'), 52, 125)
(('4', '5', '8', '9'), 54, 129)
(('4', '6', '7', '8'), 53, 122)
(('4', '6', '7', '9'), 56, 135)
(('5', '6', '7', '8'), 58, 130)
(('5', '6', '8', '9'), 66, 143)
'''

class Stack:
	def __init__(self):
		self.items = list()

	def is_empty(self):
		return len(self.items) == 0

	def pop(self):
		return self.items.pop()

	def push(self,item):
		return self.items.append(item)

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)

def infix_to_postfix(infix_expr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1

	op_stack = Stack()
	postfix_list = []
	token_list = infix_expr.split()
	for token in token_list:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfix_list.append(token)
		elif token == '(':
			op_stack.push(token)
		elif token == ')':
			top_token = op_stack.pop()
			while top_token != '(':
				postfix_list.append(top_token)
				top_token = op_stack.pop()
		else:
			while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
				postfix_list.append(op_stack.pop())
			op_stack.push(token)

	while not op_stack.is_empty():
		postfix_list.append(op_stack.pop())

	return " ".join(postfix_list)

def do_math(op, op1, op2):
	if op == "*":
		return op1 * op2
	elif op == "/":
		return op1 / op2
	elif op == "+":
		return op1 + op2
	else:
		return op1 - op2


def postfix_eval(postfix_expr):
	operand_stack = Stack()
	token_list = list(postfix_expr)
	# token_list = postfix_expr.split()
	for token in token_list:
		if token in "0123456789":
			operand_stack.push(int(token))
		else:
			operand2 = operand_stack.pop()
			operand1 = operand_stack.pop()
			result = do_math(token, operand1, operand2)
			operand_stack.push(result)

	return operand_stack.pop()

op_combos = list(itertools.product('+-/*',repeat = 3))

def all_combos(num_combo):
	result_combos = []

	for x in xrange(0,len(op_combos)):
		given_combos = list(num_combo) + list(op_combos[x])
		result_combos += itertools.permutations(given_combos)
	return result_combos
	
def main():
	digits = map(str,list(range(1,10)))
	digit_combos = itertools.combinations(digits,4) # Default output is a tuple
	
	longest_length = 0
	result = []
	for combo in digit_combos:
		postfix_eqns = all_combos(combo)

		entries = set()
		for eqn in postfix_eqns:
			eqn = ''.join(eqn)

			try:
				eqn_result = int(postfix_eval(eqn))
				if eqn_result >= 1 and eqn_result%1 == 0:
					entries.add(eqn_result)
			except:
				continue
		
		entries = sorted(entries)
		consecutive = True
		i = 1
		while(consecutive):
			if entries[:i] == list(range(1,i+1)):
				pass
			else:
				consecutive = False
				length = i
			i += 1
		
		if length > longest_length:
			longest_length = length
			result = combo

	return result

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))


'''
(('1', '2', '5', '8'), 51)
(('2', '6', '8', '9'), 56)
(('3', '4', '6', '7'), 51)
(('3', '5', '6', '8'), 58)
(('4', '5', '6', '8'), 52)
(('4', '5', '7', '8'), 51)
(('4', '5', '7', '9'), 51)
(('4', '5', '8', '9'), 53)
(('4', '6', '7', '8'), 52)
(('4', '6', '7', '9'), 55)
(('5', '6', '7', '8'), 57)
(('5', '6', '8', '9'), 65)
'''