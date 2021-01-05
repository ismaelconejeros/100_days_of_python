#You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 2 and 100.

##e.g. 2 + 4 + 6 + 8 +10 ... + 98 + 100

#Important, there should only be 1 print statement in your console output. 
# It should just print the final total and not every step of the calculation.

#Hint
#There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.

#Write your code below this row 👇

sum_even = 0

for i in range(0,101,2):
	sum_even += i

print(sum_even)

#--------------

suma_even = 0

for i in range(0,101):
	if i%2 == 0:
		suma_even += i

print(suma_even)