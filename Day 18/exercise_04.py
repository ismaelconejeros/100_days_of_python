#Draw a random walk with turtles
import random
import turtle

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def random_walk(name):
    name.pensize(5)
    name.speed(5)
    name.shape(random.choice(['triangle', 'circle', 'square', 'turtle']))
    name.color(random_color())
    name.left(random.randint(1,360))
    name.forward(random.randint(5,40))

tam = turtle.Turtle()
tem = turtle.Turtle()
tim = turtle.Turtle()
tom = turtle.Turtle()
tum = turtle.Turtle()

while True:
    random_walk(tam)
    random_walk(tem)
    random_walk(tim)
    random_walk(tom)
    random_walk(tum)
    
my_screen = turtle.Screen()
my_screen.exitonclick()