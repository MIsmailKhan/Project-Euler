import math 
import time
start = time.time()

def main():
    largest=int()      
    for i in xrange(9000,10000):
        temp=str(i)+str(i*2)
        if "0" not in temp:
            if len(set(temp))==9:
                if int(temp)>largest:
                    largest=int(temp)

    return largest 
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))