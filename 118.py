import math
import time
import itertools
start = time.time()

# Particularlyt ineffective solution
# http://www.mathblog.dk/project-euler-118-sets-prime-elements/

def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller

def join_list_elements(list_partitions):
	result = list()
	for entry in list_partitions:
		concatenated_string = ''.join(map(str, entry))
		result.append(concatenated_string)
	return frozenset(result)

def is_prime(n):
    # n = abs(n)
    if n<=1: 
        return False
    for i in range(2,(int(math.sqrt(n))+1)):
        if n%i == 0:
            return False
            break
    return True

def main():
	count = 0
	pandigitals = list(range(1,10))
	all_possibilities = [list(x) for x in itertools.permutations(pandigitals)]
	all_distinct_sets = set()
	for i,possibility in enumerate(all_possibilities):
		print(i)
		for entry in partition(possibility):
			all_distinct_sets.add(join_list_elements(entry))

	print(len(all_distinct_sets))


'''
			flag = True
			previous = entry[0]
			for element in entry[1:]:
				if element > previous:
					previous = element
					if is_prime(int(element)):
						continue
				else:
					flag = False
					break

			if flag == True:
				count += 1
			

	return count
'''
			
			
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))