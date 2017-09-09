import time
start=time.time()

def sumfact(n):
	sum=1,
	digit=0
	digisum=0
	for i in range(n,1):
		sum=sum*i
	while(sum!=1):
		digit=sum%10
		digisum=digisum+digit
		sum=sum/10
	return(digisum)


ans=sumfact(2)

stop=(time.time()-start)
print(('%s found in %s seconds')%(ans,stop))
