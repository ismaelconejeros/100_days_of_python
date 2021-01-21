from turtle import Turtle
import random

WIDTH = 900
HEIGHT = 450
CAR_COLORS = ['black', 'red', 'orange', 'blue', 'purple', 'white']

class Chicken(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0, -HEIGHT+20)

    def move_up(self):
        self.setheading(90)
        self.forward(10)
    def move_down(self):
        self.setheading(270)
        self.forward(10)
    def move_left(self):
        self.setheading(180)
        self.forward(10)
    def move_right(self):
        self.setheading(0)
        self.forward(10)

    def new_level(self):
        self.goto(0, -HEIGHT+20)

class Cars():
    def __init__(self):
        self.cars = []
        self.create_cars()
        self.car_speed = 0.5

    def create_cars(self):
        n_cars = random.randint(round((WIDTH/HEIGHT)*5),round((WIDTH/HEIGHT)*10))
        for i in range(n_cars):
            y_place = random.randint(-HEIGHT+50, HEIGHT-50)
            x_place = random.randint(-WIDTH, WIDTH*3)
            car = Turtle('square')
            car.color(random.choice(CAR_COLORS))
            car.penup()
            car.shapesize(1,random.choice([2,3,4,5]))
            car.setheading(180)
            car.goto(x_place, y_place)
            self.cars.append(car)

    def move(self):
        x_place = random.randint(WIDTH, WIDTH*3)
        y_place = random.randint(-HEIGHT+50, HEIGHT-50)
        for i in self.cars:
            i.forward(self.car_speed)
            if i.xcor() < -WIDTH:
                i.goto(x_place, y_place)

    def car_levelup(self):
        for i in self.cars:
            self.car_speed += 0.01


class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.color('black')
        self.pensize(1)
        self.create_map()
    
    def create_map(self):
        distance = 40
        for i in range(1,round(HEIGHT/distance)-1):
            self.goto(WIDTH, -HEIGHT + distance*i)
            self.pendown()
            self.goto(-WIDTH, -HEIGHT + distance*i)
            self.penup()
        for i in range(1,round(HEIGHT/distance)-1):
            self.goto(WIDTH, HEIGHT - distance*i)
            self.pendown()
            self.goto(-WIDTH, HEIGHT - distance*i)
            self.penup()
        
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.goto(-WIDTH+100, HEIGHT-50)
        self.stage = 0
        self.update_score()

    def update_score(self):
        self.stage += 1
        self.clear()
        self.write(f"Stage: {self.stage}", move=False, align="center", font=("Courier", 28, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align="center", font=("Courier", 45, "bold"))


