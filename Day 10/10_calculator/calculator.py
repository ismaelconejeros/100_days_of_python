from art import logo
from replit import clear

print(logo)

def add(n1, n2):
    '''n1 + n2'''
    return n1 + n2

def substract(n1, n2):
    '''n1 - n2'''
    return n1 - n2

def multiply(n1, n2):
    '''n1 * n2'''
    return n1 * n2

def divide(n1, n2):
    '''n1 / n2'''
    return n1 / n2

operations = {'+': add, '-': substract, '*': multiply, '/': divide}

answer = 0
calc_on = True
num1 = float(input('What\'s the first number? '))

while calc_on:
	operation_symbol = input('Pick an operation: ')
	num2 = float(input('What\'s the second number? '))
	answer = operations[operation_symbol](num1, num2)
	print(f'{num1} {operation_symbol} {num2} = {answer:.2f}')

	again = input(f'Do you want to continue operating with {answer:.2f}? (Y)\nOr do you want to start again? (N)\n').lower()
	if again == 'y':
		num1 = answer
	elif again == 'n':
		clear()
		answer = 0
		print(logo)
		num1 = int(input('What\'s the first number? '))
	else:
		calc_on = False