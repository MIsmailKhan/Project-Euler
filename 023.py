import math
import time
# from  more_itertools import unique_everseen

start = time.time()

def factors(n):
	result = [1]
	for i in range(2,(n//2)+1):

		if i in result:
			break

		if n%i == 0:
			result.extend((i,(n/i)))

	result = list(set(result))
	return result

def check_abundant(n):
	if n < 12:
        return False
    return sum(factors(n)) > n

def create_abundant_list(n_range):
	return list(x for x in range(1, n_range) if is_abundant(x))

def sum_abundant(abundant_list):
	result = []
	for element in abundant_list:
		for another_element in abundant_list:
			result.append(element+another_element)
	return result

def main(n):
	answer = 0
	list_numbers = create_abundant_list(n)
	sum_abundant_numbers = sum_abundant(list_numbers)
	for i in range(n):
		if i in sum_abundant_numbers:
			pass
		else:
			answer += i
	return answer

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(28123),elapsed)) 