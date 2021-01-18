import turtle
import random
import time

turtle.resizemode("user")

def set_goal():
    goal.speed(3)
    goal.pensize(8)
    goal.penup()
    goal.goto(400, -300)
    goal.left(90)
    goal.pendown()
    goal.goto(400, 300)

def color_change():
    for i in turtle_list:
        i.shape('turtle')
        i.shapesize(3,3, 7)
        color_t = random.choice(available_colors)
        i.color(color_t)
        available_colors.remove(color_t)
        participants[i] = color_t

def set_turtles():
    for i in turtle_list:
        spot = random.choice(start_spots)
        start_spots.remove(spot)
        i.penup()
        i.goto(-300, spot)
        i.pendown

def race():
    global winner
    race_on = True
    while race_on:
        turt = random.choice(turtle_list)
        steps = random.choice([1, 7,10,15])
        turt.forward(steps)
        if turt.xcor() >= 400:
            race_on = False
            winner = turt

goal = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()

screen = turtle.Screen()
screen.screensize(500, 500, 'PaleGreen')

repeat = True
while repeat:
    turtle_list = [t1, t2, t3, t4, t5, t6]
    available_colors = ['red', 'blue', 'green', 'purple', 'yellow', 'white']
    start_spots = [-210, -140, -70, 0, 70, 140]
    participants = {}
    winner = ""

    bet = screen.textinput("TURTLE RACE", f"Which color will you bet to be the winner?\n{available_colors}").lower()
    color_change()
    set_goal()
    set_turtles()
    time.sleep(1)
    race()

    if bet == participants[winner]:
        result = screen.textinput("The result is:", f"YOU WIN!\nThe winner is the {bet.title()} Turtle\n\nPress Y to play again").lower()
    else:
        result = screen.textinput("The result is:", f"YOU LOSE!\nThe winner is the {participants[winner].title()} Turtle\n\nPress Y to play again").lower()
    
    if result != 'y':
        repeat = False

screen.exitonclick()




