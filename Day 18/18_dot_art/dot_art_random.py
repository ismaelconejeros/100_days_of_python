import random
import turtle

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

x = -300
y = -200
steps = 50

dot = turtle.Turtle()
dot.shape('circle')
dot.speed(5)

for j in range(round((x*-2)/steps)):
    dot.penup()
    dot.goto(x, y)
    for i in range(round((x*-2)/steps)):
        dot.color(random_color())
        dot.stamp()
        dot.forward(steps)
    y += steps

my_screen = turtle.Screen()
my_screen.exitonclick()