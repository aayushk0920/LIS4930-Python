import fileinput
from datetime import datetime

#part1
#get the current date and time
current_datetime = datetime.now()
current_date = current_datetime.strftime('%Y-%m-%d')
current_time = current_datetime.strftime('%H:%M:%S')

#Initialize variables with default values
print("=== Part 1 ===")
date = current_date
time = current_time
with fileinput.input(files='module6data.txt') as file:
    for line in file:
        data = line.split()
        if len(data) == 6:
            _, _, store, item, cost, payment = data
            print("{0}\t{1}".format(item, cost))
    print("{0}\t{1}".format(date, time))
#part2
print("=== Part 2 ===")
from datetime import datetime, timedelta
 
#subtract 60 seconds from current time
print(datetime.now() - timedelta(seconds=60))
 
#add two years to current date
print(datetime.now() + timedelta(days=720))
#part3
print("=== Part 3 ===")
from datetime import timedelta
 
# create the time delta object for 100 days, 10 hours, and 13 minutes
d = timedelta(days=100, hours=10, minutes=13)
 
# Will print the timedelta object
print(d)
 
# print only the day component of the timedelta object
print(d.days)
 
# Redefines components of the timedelta object
days = d.days
seconds = d.seconds
microseconds = d.microseconds
 
print((days, seconds, microseconds))
#part4
print("=== Part 4 ===")
from datetime import datetime
 
time_now = datetime.now()
 
 
def growth_tracker():
    print("Let's track your growth. How tall are you in feet & inches?")
    feet = int(input("How many feet? "))
    inches = int(input("How many inches? "))
    print("At " + str(time_now) + " you are " + str(feet) + " feet, " + str(inches) + " inches.")
 
 
growth_tracker()
