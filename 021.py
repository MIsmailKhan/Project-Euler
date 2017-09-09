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

def amicable(n):
	check = sum(factors(n))
	check_2 = sum(factors(check))
	if n == check_2:
		if check == check_2:
			return 0,0
		else:
			return check,check_2
	else:
		return 0,0


amicable_list = [220]
for i in range(220,10000):
	if i not in amicable_list:
		amicable_list.extend((amicable(i)))

amicable_list = list(set(amicable_list))
print (amicable_list)
answer = sum(amicable_list)

# 496, 8128 are not amicable numbers
elapsed = time.time() - start
print ("%s found in %s seconds" % (answer,elapsed)) 

			