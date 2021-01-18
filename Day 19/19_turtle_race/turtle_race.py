from turtle import Turtle, Screen
import random
import time

goal = Turtle()
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()

turtle_list = [t1, t2, t3, t4, t5, t6]
available_colors = ['red', 'blue', 'green', 'purple', 'yellow', 'white']
start_spots = [-210, -140, -70, 0, 70, 140]
participants = {}
winner = ""

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

screen = Screen()
screen.screensize(500, 500, 'lightgreen')
bet = screen.textinput("TURTLE RACE", "Which color will you bet to be the winner?").lower()

color_change()
set_goal()
set_turtles()
time.sleep(1)
race()

if bet == participants[winner]:
    print("YOU WIN!")
    print(f"{bet} is the winner!")
else:
    print("YOU LOSE!")
    print(f"You bet on {bet.title()}")
    print(f"The winner is: {participants[winner].title()}")


screen.exitonclick()




