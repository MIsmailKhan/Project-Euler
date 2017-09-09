import itertools
import time


start = time.time()

answer_list = list(itertools.permutations('0123456789'))
solution = ''.join(answer_list[999999])

elapsed = time.time() - start
print ("%s found in %s seconds" % (solution,elapsed)) 

