#Write your code below this line 👇

def prime_checker(number):
	counter = 0
	dividers = []
	for i in range(1,number+1):
		if number%i == 0:
			counter +=1
			dividers.append(i)
	if counter == 2:
		print(f'the number {number} is a prime number.')
	else:
		print(f'the number {number} is not a prime number.')
		print(f'it can be divided by {dividers}')

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
