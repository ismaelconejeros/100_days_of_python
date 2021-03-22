from turtle import Turtle, Screen
from tic_tac_toe_classes import WIDTH, HEIGHT, Board, CircleRed, CircleBlue
import random

screen = Screen()
screen.setup(900, 900)
screen.screensize(WIDTH*2, HEIGHT*2, 'lightgreen')
screen.tracer(0)

board = Board()
player = CircleBlue()
player2 = CircleRed()

screen.onkeypress(player.one, "1")
screen.onkeypress(player.two, "2")
screen.onkeypress(player.three, "3")
screen.onkeypress(player.four, "4")
screen.onkeypress(player.five, "5")
screen.onkeypress(player.six, "6")
screen.onkeypress(player.seven, "7")
screen.onkeypress(player.eight, "8")
screen.onkeypress(player.nine, "9")


screen.onkeypress(player2.one, "z")
screen.onkeypress(player2.two, "x")
screen.onkeypress(player2.three, "c")
screen.onkeypress(player2.four, "a")
screen.onkeypress(player2.five, "s")
screen.onkeypress(player2.six, "d")
screen.onkeypress(player2.seven, "q")
screen.onkeypress(player2.eight, "w")
screen.onkeypress(player2.nine, "e")

def check_win():
    game_on = True
    player.used_squares.sort()
    player2.used_squares.sort()
    game = player.used_squares + player2.used_squares
    unique = []
    winning_sets = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,7],[3,6,9],[1,5,9],[3,5,7]]
    for i in game:
        if i not in unique:
            unique.append(i)
            unique.sort()
    if len(unique) < len(game):
        player.goto(0,0)
        player.color('orange')
        player.write("Invalid Move", move=False, align="center", font=("Arial", 40, "bold"))
        game_on = False
    elif player.used_squares in winning_sets:
        player.goto(0,0)
        player.color('orange')
        player.write("Player 1 WINS", move=False, align="center", font=("Arial", 40, "bold"))
        game_on = False
    elif player2.used_squares in winning_sets:
        player2.goto(0,0)
        player2.color('orange')
        player2.write("Player 2 WINS", move=False, align="center", font=("Arial", 40, "bold"))
        game_on = False
    return game_on


screen.listen()
game_on = True
while game_on:
    screen.update()
    game_on = check_win()
screen.exitonclick()