import turtle
import random

snake_cords = [(0,0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
        self.score = 0

    def create_snake(self):
        for i in snake_cords:
            snake = turtle.Turtle('square')
            snake.color('white')
            snake.penup()
            snake.speed(9)
            snake.goto(i)
            self.parts.append(snake)

    def add_new_part(self):
        snake = turtle.Turtle('square')
        snake.color('white')
        snake.speed('fastest')
        snake.penup()
        snake.goto(self.parts[-1].pos())
        self.parts.append(snake)

    def move(self):
        for i in range(len(self.parts)-1, 0, -1):
            new_x = round(self.parts[i-1].xcor())
            new_y = round(self.parts[i-1].ycor())
            self.parts[i].goto(new_x, new_y)
        self.parts[0].goto(round(self.parts[0].xcor()),round(self.parts[0].ycor()))
        self.parts[0].forward(20)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def reset(self):
        for part in self.parts:
            part.goto(2000,2000)
        self.parts.clear()
        self.create_snake()
        self.head = self.parts[0]

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        randomx = random.randint(-280,280)
        randomy = random.randint(-280,280)
        self.goto(randomx, randomy)

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.clear()
        self.speed('fastest')
        self.goto(-0,100)
        self.score = 0
        self.highscore = 0
        self.read_highscore()
        self.write(f"Score: {self.score} - High Score: {self.highscore}", move=False, align="center", font=("Courier", 18, "normal"))

    def read_highscore(self):
        with open('C:/Users/isma/Desktop/VSC/100_days_of_python/100_days_of_python/Day 24/24_better_snake/highscore.txt') as file:
            highscore_text = file.read()
            self.highscore = int(highscore_text)

    def set_highscore(self):
        with open('C:/Users/isma/Desktop/VSC/100_days_of_python/100_days_of_python/Day 24/24_better_snake/highscore.txt', mode='w') as file:
            highscore = str(self.score)
            file.write(highscore)

    def score_up(self):
        self.clear()
        self.read_highscore()
        self.write(f"Score: {self.score} - High Score: {self.highscore}", move=False, align="center", font=("Courier", 18, "normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!", move=False, align="center", font=("Arial", 35, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.set_highscore()
        self.score = 0
        self.score_up()

class Margin(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.speed('fast')
        self.hideturtle()
        self.goto(300,-300)
        self.pendown()
        self.goto(300,300)
        self.goto(-300,300)
        self.goto(-300,-300)
        self.goto(300,-300)