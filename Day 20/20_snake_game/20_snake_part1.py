import turtle
import random
import time

snake_cords = [(0,0), (-20, 0), (-40, 0)]

screen = turtle.Screen()
screen.screensize(600, 600, "black")

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

class Food:
    def __init__(self):
        self.history = []
        self.new_food()
        self.last_food = self.history[0]
        self.score = 0

    def new_food(self):
        x_food = random.choice([-20,20]) * random.randint(0,15)
        y_food = random.choice([-20,20]) * random.randint(0,15)
        food = turtle.Turtle()
        food.shape('circle')
        food.speed('fastest')
        food.color('red')
        food.penup()
        food.goto(x_food, y_food)
        self.history.append(food)
        self.last_food = self.history[len(self.history)-1]

    def add_point(self):
        self.score += 1
        print(f'Score: {self.score}')


snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")
screen.onkey(snake.move_down,"Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    print(f"{snake.head.xcor()},{snake.head.ycor()}")

    if snake.head.position() == food.last_food.position():
        food.last_food.ht()
        food.new_food()
        food.add_point()
        snake.add_new_part()

    if snake.head.xcor() < -450 or snake.head.xcor() > 450 or snake.head.ycor() < -450 or snake.head.ycor() > 450:
        game_on = False

screen.exitonclick()