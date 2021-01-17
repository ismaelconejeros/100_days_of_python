#Draw a dashed line square with turtle

from turtle import Turtle, Screen

tom = Turtle()
tom.shape('turtle')

for j in range(4):
    for i in range(11):
        tom.forward(10)
        tom.penup()
        tom.forward(10)
        tom.pendown()
    tom.left(90)

my_screen = Screen()
my_screen.exitonclick()