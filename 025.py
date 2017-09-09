import time 

start = time.time()
''' 
# fibonacci using recursion, too long
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1: 
		return 1
	else:
	 	return fibonacci(n-1)+fibonacci(n-2)

'''

def find_fibonacci():

    a, b = 0, 1
    flag = True
    count = 0

    while flag is True:
        x = str(a)
        if len(x) == 1000:
        	elapsed = time.time() - start
	        print (count)
	        flag = False

        a, b, = b, a + b
        count += 1

find_fibonacci()