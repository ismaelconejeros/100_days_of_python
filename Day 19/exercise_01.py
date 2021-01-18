#Move the arrow forward with keyboard

from turtle import Turtle, Screen

tom = Turtle()

def move_forward():
    tom.forward(10)

screen = Screen()
screen.listen()
screen.onkey(key='space', fun=move_forward)

screen.exitonclick()