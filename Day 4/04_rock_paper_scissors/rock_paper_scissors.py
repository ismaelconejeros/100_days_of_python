import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]


print('ROCK, PAPER and SCISSORS')
print('Choose (1) for rock, (2) for paper and (3) for scissors')
print()
person = input('Your choice:  ')
print()

if person == '1':
	person = rock
elif person == '2':
	person = paper
elif person == '3':
	person = scissors


print(person)
print()
print('The computer choice is:')
computer = random.choice(options)
print(computer)
print()

if person == computer:
	print('IT\' A TIE!')
elif person == rock and computer == scissors:
	print('YOU WIN')
elif person == paper and computer == rock:
	print('YOU WIN')
elif person == scissors and computer == paper:
	print('YOU WIN')
else:
	print('YOU LOSE!')