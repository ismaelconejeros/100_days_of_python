#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon with turtle


from turtle import Turtle, Screen
import random

tom = Turtle()

start_sides = 3
colors = ["red","orange","yellow","green","blue","indigo","purple"]
tom.sety(100)

for i in range(start_sides, 11):
    for j in range(i):
        tom.forward(100)
        tom.right(360/i)
        tom.color(random.choice(colors))

my_screen = Screen()
my_screen.exitonclick()