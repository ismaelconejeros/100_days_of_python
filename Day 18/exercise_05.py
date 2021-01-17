#Draw a spirograph
import random
import turtle

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

tom = turtle.Turtle()
tom.shape('turtle')
tom.speed(0.5)

while True:
    tom.color(random_color())
    tom.circle(100)
    tom.left(5)

my_screen = turtle.Screen()
my_screen.exitonclick()