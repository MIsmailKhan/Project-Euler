import time,calendar


#time at the start of execution
start = time.time()

#changing the preference from monday to sunday
calendar.setfirstweekday(6)


def sundays(year):
	"""This function returns 
	The number of sundays in a year
	on the first of the month"""
	counter = 0
	for month in xrange(1,13):
		cal = calendar.monthcalendar(year,month)
		if cal[0][0]:
			counter += 1
	return counter

#let the total number of sundays be 0
total = 0

#counting the sundays that fell on 
#first of every month for each year
for i in xrange(1901,2001):
	total += sundays(i)

#time at the end of execution
end = time.time()

#printing the output along with exection time
print "Found {} in {} seconds".format(total,end-start)

'''
from datetime import date
from collections import Counter

counter = Counter()

for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        day = date(year, month, 1)
        counter[day.weekday()] += 1

print counter[6]
'''
