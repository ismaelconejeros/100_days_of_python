import random
from art import logo
from game_data import *
from replit import clear


game_on = True

points = 0

while game_on:
    game_stage = 0
    while game_stage == 0: #NEW GAME
        points = 0
        game_stage = 1 

    while game_stage ==1: #FIRST
        left = random.choice(data)
        right = random.choice(data)
        last = 0

        clear()
        print(logo)
        print(f'You have {points} points.\n')
        pick = input(f"Who has more followers?\n (1) - {left['name']}, a {left['description']} from {left['country']}\n (2) - {right['name']}, a {right['description']} from {right['country']}\n")
        if pick == '1':
            if left['follower_count'] > right['follower_count']:
                points += 1
                last = left
                game_stage = 2
            elif left['follower_count'] < right['follower_count']:
                again = input('Press any key to continue...')
                print(f"NO!, {left['name']} has {left['follower_count']}, meanwhile {right['name']} has {right['follower_count']}.")
                game_stage = 0
                again = input('\nPress any key to continue...')
        elif pick == '2':
            if left['follower_count'] < right['follower_count']:
                points += 1
                last = right
                game_stage = 2
            elif left['follower_count'] > right['follower_count']:
                print(f"NO!, {right['name']} has {right['follower_count']}, meanwhile {left['name']} has {left['follower_count']}.")
                game_stage = 0
                again = input('\nPress any key to continue...')

    while game_stage == 2: #CONTINUE
        clear()
        print(logo)
        next_pick = random.choice(data)
        print(f'You have {points} points.\n')
        pick = input(f"Okay, now who has more followers?\n (1) - {last['name']}\n (2) - {next_pick['name']}\n")
        if pick == '1':
            if last['follower_count'] > next_pick['follower_count']:
                points += 1
            elif last['follower_count'] < next_pick['follower_count']:
                print(f"NO!, {last['name']} has {last['follower_count']}, meanwhile {next_pick['name']} has {next_pick['follower_count']}.")
                game_stage = 0
                again = input('\nPress any key to continue...')
        elif pick == '2':
            if last['follower_count'] < next_pick['follower_count']:
                points += 1
                last = next_pick
            elif last['follower_count'] > next_pick['follower_count']:
                print(f"NO!, {next_pick['name']} has {next_pick['follower_count']}, meanwhile {last['name']} has {last['follower_count']}.")
                game_stage = 0
                again = input('\nPress any key to continue...')