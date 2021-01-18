from turtle import Turtle, Screen

pen = Turtle()

def pen_up():
    pen.penup()

def pen_down():
    pen.pendown()

def move_forward():
    pen.forward(10)

def move_right():
    pen.right(5)

def move_left():
    pen.left(5)

def clear():
    pen.clear()
    pen.penup()
    pen.home()
    pen.down()

screen = Screen()
screen.onkey(pen_up, "Up")
screen.onkey(pen_down, "Down")
screen.onkeypress(move_forward, "space")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkey(clear, "c")
screen.listen()

screen.exitonclick()