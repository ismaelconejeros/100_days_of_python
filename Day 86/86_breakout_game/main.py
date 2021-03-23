from turtle import Turtle, Screen
import random


WIDTH = 900
HEIGHT = 500

screen = Screen()
screen.setup(WIDTH*2, HEIGHT*2)
screen.screensize(WIDTH*2, HEIGHT*2, 'lightblue')
screen.tracer(0)

class PlayerPad(Turtle):
    def __init__(self):
        super().__init__()
        #self.resizemode("user")
        self.penup()
        self.shape("square")
        self.turtlesize(2,8)
        #self.shapesize(2,8)
        self.setposition(0,-HEIGHT+120)
        self.steps = 15
    def move_left(self):
        x = self.xcor()
        x -= self.steps
        if x < -WIDTH+180:
            x=-WIDTH+180
        self.setx(x)
    def move_right(self):
        x = self.xcor()
        x += self.steps
        if x > WIDTH-180:
            x = WIDTH-180
        self.setx(x)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.speed(9)
        self.setposition(0,-HEIGHT+150)
        self.setheading(random.randint(15,165))

    def move(self):
        self.forward(2)
        if self.xcor() >= WIDTH-110:
            self.move_left()
        elif self.xcor() <= -WIDTH+110:
            self.move_right()
        elif self.ycor() >= HEIGHT-110:
            self.move_down()

    def move_left(self):
        if self.heading() < 90:
            direction = random.randint(160, 200)
            self.setheading(direction)
        else:
            direction = random.randint(200,240)
            self.setheading(direction)

    def move_right(self):
        if self.heading() < 180:
            direction = random.randint(20,60)
            self.setheading(direction)
        else:
            direction = random.randint(290,330)
            self.setheading(direction)

    def move_down(self):
        if self.heading() < 90:
            direction = random.randint(290,330)
            self.setheading(direction)
        else:
            direction = random.randint(200,240)
            self.setheading(direction)

    def move_up(self):
        if self.heading() < 270:
            direction = random.randint(110,150)
            self.setheading(direction)
        else:
            direction = random.randint(20,60)
            self.setheading(direction)

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(3)
        self.penup()
        self.setposition(-WIDTH + 100, -HEIGHT + 100)
        self.pendown()
        self.setposition(WIDTH - 100, -HEIGHT + 100)
        self.setposition(WIDTH - 100, HEIGHT - 100)
        self.setposition(-WIDTH + 100, HEIGHT - 100)
        self.setposition(-WIDTH + 100, -HEIGHT + 100)

class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.colors = ["red", "blue", "purple", "green", "yellow"]
        self.color(random.choice(self.colors))
        self.shape("square")
        self.penup()
        self.turtlesize(1,2)

class Blocks:
    def __init__(self):
        self.block_list = []
        self.row()

    def row(self):
        y = 0
        x = -WIDTH + 200
        for i in range(10):
            for j in range(29):
                new_block = Block()
                new_block.setposition(x,y)
                self.block_list.append(new_block)
                x += 50
            x = -WIDTH + 200
            y += 30


board = Board()
playerpad = PlayerPad()
ball = Ball()
blocks = Blocks()

screen.listen()
screen.onkeypress(playerpad.move_left, "Left")
screen.onkeypress(playerpad.move_right, "Right")
game_on = True
while game_on:
    screen.update()
    ball.move()
    if ball.distance(playerpad) <= 50:
       ball.move_up()
    if ball.ycor() < -HEIGHT-50:
        ball.setposition(playerpad.xcor(), playerpad.ycor()+51)
    for block in blocks.block_list:
        if ball.distance(block) <= 20:
            block.hideturtle()

screen.exitonclick()