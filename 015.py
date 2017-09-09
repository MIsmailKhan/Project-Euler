import time
'''def power(n):
    sum=1
    for i in range(1,n):
        sum*=2
    sumdigit=digit(sum)
    return (sumdigit)

def digit(x):
    sum1=0
    while(x>=1):
        rem=x%10
        sum1+=rem
        x=x/10
    return(sum1)

start=time.time()
ans=power(1000)
elapsed=(time.time()-start)
print ("%s found in %s seconds",(ans,elapsed))'''

import time
 
def pow2sum(exp):
    pow = list(str(2**1000))
    return sum([int(i) for i in pow])
 
start = time.time()
n = pow2sum(1000)
elapsed = (time.time() - start)
print ("%s found in %s seconds" % (n,elapsed))
