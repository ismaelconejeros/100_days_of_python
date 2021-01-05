# Password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '?']


def createpass(n):
    listpass = []
    for elem in range(n-5):
        listpass.append(random.choice(letters))
    for elem in range(n-7):
        listpass.append(random.choice(numbers))
    for elem in range(n-8):
        listpass.append(random.choice(symbols))
    random.shuffle(listpass)
    password = "".join(listpass)
    print(password)


print('How long must be your password?')
lenght = int(input())

createpass(lenght)

