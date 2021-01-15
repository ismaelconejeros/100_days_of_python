from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('DarkOrchid4')
while True:
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()