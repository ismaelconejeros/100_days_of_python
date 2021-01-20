from turtle import Turtle
import random

WIDTH = 600
HEIGHT = 300
BALLSPEED = 2
POSITIONS = [(-WIDTH+10,-40), (-WIDTH+10,-20),(-WIDTH+10,0), (-WIDTH+10,20), (-WIDTH+10,40)]

class PaddleUser:
    def __init__(self):
        self.paddle = []
        self.create_paddle()
        self.paddle_main = self.paddle[1]

    def create_paddle(self):
        for i in POSITIONS:
            paddle_part = Turtle("square")
            paddle_part.color('white')
            paddle_part.penup()
            paddle_part.speed('fastest')
            paddle_part.goto(i)
            self.paddle.append(paddle_part)

    def move_up(self):
        if self.paddle_main == self.paddle[len(self.paddle)-1]:
            for i in range(len(self.paddle)):
                x = self.paddle[i].xcor()
                new_y = self.paddle[i].ycor() + 20
                self.paddle[i].goto(x, new_y)
            self.paddle_main = self.paddle[1]
    
    def move_down(self):
        if self.paddle_main == self.paddle[0]:
            for i in range(len(self.paddle)):
                x = self.paddle[i].xcor()
                new_y = self.paddle[i].ycor() - 20
                self.paddle[i].goto(x, new_y)
            self.paddle_main = self.paddle[1]

    def move(self):
        if self.paddle[0].ycor() > -HEIGHT and self.paddle[len(self.paddle)-1].ycor() < HEIGHT:
            self.move_up()
            self.move_down()
        elif self.paddle[0].ycor() <= -HEIGHT:
            self.move_up()
        elif self.paddle[len(self.paddle)-1].ycor() >= HEIGHT:
            self.move_down()

    def up(self):
        self.paddle_main = self.paddle[len(self.paddle)-1]

    def down(self):
        self.paddle_main = self.paddle[0]

class PaddlePC(PaddleUser):
    def __init__(self):
        super().__init__()
        self.paddle_main = self.paddle[len(self.paddle)-1]

    def create_paddle(self):
        super().create_paddle()
        dist = 20
        for i in range(len(self.paddle)):
            self.paddle[i].goto(WIDTH-10,-dist)
            self.paddle[i].setheading(90)
            dist += 20
        
    def go_center(self):
        dist = 20
        for i in range(len(self.paddle)):
            self.paddle[i].goto(WIDTH-10,-dist)
            self.paddle[i].setheading(90)
            dist += 20

    def move(self):
        for i in range(len(self.paddle)):
            self.paddle[i].forward(1)
        if self.paddle[0].ycor() >= HEIGHT:
            self.go_down()
        elif self.paddle[len(self.paddle)-1].ycor() <= -HEIGHT:
            self.go_up()

    def go_up(self):
        for i in range(len(self.paddle)):
            self.paddle[i].setheading(90)
    
    def go_down(self):
        for i in range(len(self.paddle)):
            self.paddle[i].setheading(270)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('orange')
        self.penup()
        self.speed(0)
        self.goto(WIDTH-30, 0)

    def move(self):
        self.forward(BALLSPEED)
        if self.ycor() >= HEIGHT or self.ycor() <= -HEIGHT:
            self.setheading(-self.heading())

    def move_left(self):
        direction = random.randint(160, 200)
        self.setheading(direction)

    def move_right(self):
        direction = random.choice([random.randint(0,20), random.randint(340,360)])
        self.setheading(direction)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.clear()
        self.speed('fastest')
        self.goto(-WIDTH/2,HEIGHT - 100)
        self.score_user = 0
        self.score_pc = 0
        self.write(f"USER\n  {self.score_user}", move=False, align="center", font=("Courier", 35, "normal"))
        self.goto(WIDTH/2,HEIGHT - 100)
        self.write(f"COMPUTER\n  {self.score_pc}", move=False, align="center", font=("Courier", 35, "normal"))

    def update_score(self):
        self.clear()
        self.goto(-WIDTH/2,HEIGHT - 100)
        self.write(f"USER\n  {self.score_user}", move=False, align="center", font=("Courier", 35, "normal"))
        self.goto(WIDTH/2,HEIGHT - 100)
        self.write(f"COMPUTER\n  {self.score_pc}", move=False, align="center", font=("Courier", 35, "normal"))

    def user_point(self):
        self.score_user += 1
        self.update_score()

    def pc_point(self):
        self.score_pc += 1
        self.update_score()

class Margin(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-WIDTH, -HEIGHT-10)
        self.pendown()
        self.color('blue')
        self.goto(-WIDTH, HEIGHT+10)
        self.goto(WIDTH, HEIGHT+10)
        self.goto(WIDTH, -HEIGHT-10)
        self.goto(-WIDTH, -HEIGHT-10)
        self.create_line()

    def create_line(self):
        self.penup()
        self.goto(0,HEIGHT)
        self.setheading(270)
        self.pensize(7)
        self.color('green')
        for i in range(round(HEIGHT/25)):
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)
