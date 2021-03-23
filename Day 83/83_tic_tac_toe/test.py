import random
from replit import clear

options = [1,2,3,4,5,6,7,8,9]

places = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}

winners = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,9]]

def print_board():
    print(f"{places[1]}|{places[2]}|{places[3]}")
    print(f"------")
    print(f"{places[4]}|{places[5]}|{places[6]}")
    print(f"------")
    print(f"{places[7]}|{places[8]}|{places[9]}")
    print("\n \n \n")

def player_turn():
    option = int(input("Choose where to play: \n"))
    options.remove(option)
    places[option] = "X"
    print_board()

def computer_turn():
    option = random.choice(options)
    options.remove(option)
    places[option] = "O"
    print_board()

def check():
    global game_on
    player_1 = 0
    player_2 = 0
    for winner_list in winners:
        for elem in winner_list:
            if places[elem] == "X":
                player_1 += 1
                if player_1 == 3:
                    print("Player 1 wins!")
                    game_on = False
                    break
            if places[elem] == "O":
                player_2 += 1
                if player_2 == 3:
                    print("Player 2 wins!")
                    game_on = False
                    break
            else:
                player_1 = 0
                player_2 = 0

clear()
print_board()
game_on = True
while game_on:
    player_turn()
    check()
    if game_on:
        clear()
        computer_turn()
    