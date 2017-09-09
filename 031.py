from itertools import permutations
import math
import time

# Very rough solution , need to improve
start = time.time()

solution = 0
for h in xrange(0,2):
	for g in xrange(0,201-((h*200))):
		for f in xrange(0,201-((g*100) + (h*200))):
			for e in xrange(0,201-((f*50) + (g*100) + (h*200))):
				for d in xrange(0,201-((e*20) + (f*50) + (g*100) + (h*200))):
					for c in xrange(0,201-((d*10) + (e*20) + (f*50) + (g*100) + (h*200))):
						for b in xrange(0,201-((c*5) + (d*10) + (e*20) + (f*50) + (g*100) + (h*200))):
							for a in range(0,201-((b*2) + (c*5) + (d*10) + (e*20) + (f*50) + (g*100) + (h*200))):
								if ((a*1) + (b*2) + (c*5) + (d*10) + (e*20) + (f*50) + (g*100) + (h*200)) == 200:
									solution += 1	


elapsed = time.time() - start
print ("%s found in %s seconds" % (solution,elapsed)) 

