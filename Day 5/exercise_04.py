#FizzBuzz
#Instructions
#You are going to write a program that automatically prints the solution to the FizzBuzz game.

#Your program should print each number from 1 to 100 in turn.

#When the number is divisible by 3 then instead of printing the number it should print "Fizz".

#`When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
#`And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

#Hint
#Remember your answer should start from 1 and go up to and including 100.
#Each number/text should be printed on a separate line.

for i in range(1,101):
	if i%5 == 0 and i%3==0:
		print(f'{i} - FIZZBUZZ')
	elif i%3 == 0:
		print(f'{i} - FIZZ')
	elif i%5 == 0:
		print(f'{i} - BUZZ')
	else:
		print(f'{i}')