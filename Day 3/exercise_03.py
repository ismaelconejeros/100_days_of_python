#Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

#This is how you work out whether if a particular year is a leap year.
#on every year that is evenly divisible by 4 
#**except** every year that is evenly divisible by 100 
#**unless** the year is also evenly divisible by 400

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year%4 == 0:
	if year%100 == 0:
		if year%400 == 0:
			print('LEAP YEAR')
		else:
			print('NOT LEAP YEAR')
	else:
		print('LEAP YEAR')
else:
	print('NOT LEAP YEAR')

#-----------------2nd way----------------------------


counter = 0

if year%4 == 0:
	counter += 1
if year%100 == 0:
	counter -= 1
if year%400 == 0:
	counter += 1

if counter > 0:
	print('LEAP YEAR')
else:
	print('NOT LEAP YEAR')