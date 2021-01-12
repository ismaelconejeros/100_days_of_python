import random
import time
from replit import clear
from art import logo

game_on = True

def lives():
    ask = input('EASY or HARD mode?\n').lower()
    if ask == 'easy':
        lives = 10
    elif ask == 'hard':
        lives = 5
    return lives

def guess():
    print(f'\nYou have {lives_num} guesses left.')
    print(f'The numbers you have guessed are: {nums}\n')
    guess = int(input('Try to guess a number: '))
    nums.append(guess)
    return guess

def check(num):
    global NUMBER, lives_num, game
    if len(nums) < 5:
        if num == NUMBER:
            print('\nYOU GOT IT\n')
            game = 0
            again = input('Press enter to play again...')
            clear()
        elif num < NUMBER:
            print('\nToo Low\n')
            lives_num -= 1
            time.sleep(1)
        else:
            print('\nToo high\n')
            lives_num -= 1
            time.sleep(1)
    else:
        if num == NUMBER:
            print('\nYOU GOT IT\n')
            game = 0
            again = input('Press enter to play again...')
            clear()
        else:
            print(f'\nYou lose, the number was {NUMBER}.\n')
            game = 0
            again = input('Press enter to play again...')
            clear()


while game_on:
    clear()
    game = 0
    print(logo)
    print('Guess a number between 1 and 100.\n')
    while game == 0:
        lives_num = lives()
        nums = []
        NUMBER = random.randint(1,100)
        game = 1
        while game == 1:
            guessed_num = guess()
            check(guessed_num)
