import random
from ascii_hangman import *
from possible_words import words
from replit import clear

def status():
    global lives, letters_guessed, word_num, letters_num
    if lives == 0:
        print('YOU LOSE')
        lives = -100
        again = input('        Do you want to start again? (Press any letter)')
    elif letters_guessed == word_num:
        print('YOU WIN')
        lives = -100
        again = input('        Do you want to start again? (Press any letter)')

def check():
    global letter, letters_list, letters_failed, lives, letters_guessed
    if letter in letters_list:
        print('You already guessed that letter')
    elif letter in letters_failed:
        print('You already FAILED on that letter')
    elif letter in word_list:
        letters_guessed += 1
        letters_list.append(letter)
    else:
        lives -= 1
        letters_failed.append(letter)
    status()

def blanks():
    global word_list, letters_list
    print(f'You have {lives} guesess left.\n')
    list_of_letters = []
    for elem in word_list:
        if elem in letters_list:
            list_of_letters.append(' ' + elem + ' ')
        else:
            list_of_letters.append(' _ ')
    word = "".join(list_of_letters)
    print(word)


while True:
    lives = -100

    while lives == -100:
        word = random.choice(words).lower()
        word_list = list(word)
        word_num = len(word_list)

        letters_guessed = 0
        letters_list = []
        letters_failed = []
        lives = 6

    while lives == 6:
        clear()
        print(title)
        print(hangman6)
        blanks()
        letter = input('Guess a letter: ').lower()
        check()
        blanks()

    while lives == 5:
        clear()
        print(title)
        print(hangman5)
        blanks()
        letter = input('Guess a letter: ').lower()
        check()
        blanks()

    while lives == 4:
        clear()
        print(title)
        print(hangman4)
        blanks()
        letter = input('Guess a letter: ').lower()
        check()
        blanks()
    
    while lives == 3:
        clear()
        print(title)
        print(hangman3)
        blanks()
        letter = input('Guess a letter: ').lower()
        check()
        blanks()
    
    while lives == 2:
        clear()
        print(title)
        print(hangman2)
        blanks()
        letter = input('Guess a letter: ').lower()
        check()
        blanks()

    while lives == 1:
        clear()
        print(title)
        print(hangman1)
        blanks()
        letter = input('Guess a letter: ').lower()
        check()
        blanks()

    while lives == 0:
        print(title)
        print(hangman0)
        blanks()
        check()