from turtle import Turtle, Screen

WIDTH = 450
HEIGHT = 450

class CircleBlue(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape('circle')
        self.speed('fastest')
        self.color('darkblue')
        self.shapesize(8,8)
        self.used_squares = []

    def stamp_in(self, num):
        if num == 1:
            self.goto(-WIDTH*2/3, HEIGHT*2/3)
        elif num == 2:
            self.goto(0, HEIGHT*2/3)
        elif num == 3:
            self.goto(WIDTH*2/3, HEIGHT*2/3)
        elif num == 4:
            self.goto(-WIDTH*2/3, 0)
        elif num == 5:
            self.goto(0,0)
        elif num == 6:
            self.goto(WIDTH*2/3, 0)
        elif num == 7:
            self.goto(-WIDTH*2/3, -HEIGHT*2/3)
        elif num == 8:
            self.goto(0, -HEIGHT*2/3)
        elif num == 9:
            self.goto(WIDTH*2/3, -HEIGHT*2/3)
        else:
            pass
        self.stamp()

    def one(self):
        self.stamp_in(1)
        self.used_squares.append(1)
    def two(self):
        self.stamp_in(2)
        self.used_squares.append(2)
    def three(self):
        self.stamp_in(3)
        self.used_squares.append(3)
    def four(self):
        self.stamp_in(4)
        self.used_squares.append(4)
    def five(self):
        self.stamp_in(5)
        self.used_squares.append(5)
    def six(self):
        self.stamp_in(6)
        self.used_squares.append(6)
    def seven(self):
        self.stamp_in(7)
        self.used_squares.append(7)
    def eight(self):
        self.stamp_in(8)
        self.used_squares.append(8)
    def nine(self):
        self.stamp_in(9)
        self.used_squares.append(9)

class CircleRed(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape('circle')
        self.speed('fastest')
        self.color('red')
        self.shapesize(8,8)
        self.used_squares = []

    def stamp_in(self, num):
        if num == 1:
            self.goto(-WIDTH*2/3, HEIGHT*2/3)
        elif num == 2:
            self.goto(0, HEIGHT*2/3)
        elif num == 3:
            self.goto(WIDTH*2/3, HEIGHT*2/3)
        elif num == 4:
            self.goto(-WIDTH*2/3, 0)
        elif num == 5:
            self.goto(0,0)
        elif num == 6:
            self.goto(WIDTH*2/3, 0)
        elif num == 7:
            self.goto(-WIDTH*2/3, -HEIGHT*2/3)
        elif num == 8:
            self.goto(0, -HEIGHT*2/3)
        elif num == 9:
            self.goto(WIDTH*2/3, -HEIGHT*2/3)
        else:
            pass
        self.stamp()

    def one(self):
        self.stamp_in(1)
        self.used_squares.append(1)
    def two(self):
        self.stamp_in(2)
        self.used_squares.append(2)
    def three(self):
        self.stamp_in(3)
        self.used_squares.append(3)
    def four(self):
        self.stamp_in(4)
        self.used_squares.append(4)
    def five(self):
        self.stamp_in(5)
        self.used_squares.append(5)
    def six(self):
        self.stamp_in(6)
        self.used_squares.append(6)
    def seven(self):
        self.stamp_in(7)
        self.used_squares.append(7)
    def eight(self):
        self.stamp_in(8)
        self.used_squares.append(8)
    def nine(self):
        self.stamp_in(9)
        self.used_squares.append(9)


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color('darkblue')
        self.pensize(4)
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.goto(-WIDTH/3,HEIGHT)
        self.write("1", move=False, align="center", font=("Arial", 20, "bold"))
        self.pendown()
        self.goto(-WIDTH/3, -HEIGHT)
        self.penup()
        self.goto(WIDTH/3,HEIGHT)
        self.pendown()
        self.goto(WIDTH/3, -HEIGHT)
        self.penup()
        self.goto(-WIDTH,HEIGHT/3)
        self.pendown()
        self.goto(WIDTH, HEIGHT/3)
        self.penup()
        self.goto(-WIDTH,-HEIGHT/3)
        self.pendown()
        self.goto(WIDTH, -HEIGHT/3)
        self.penup()
        self.goto(-WIDTH*2/3, HEIGHT*2/3)
        self.write("1", move=False, align="center", font=("Arial", 20, "bold"))
        self.goto(0, HEIGHT*2/3)
        self.write("2", move=False, align="center", font=("Arial", 20, "bold"))
        self.goto(WIDTH*2/3, HEIGHT*2/3)
        self.write("3", move=False, align="center", font=("Arial", 20, "bold"))
        self.goto(-WIDTH*2/3, 0)
        self.write("4", move=False, align="center", font=("Arial", 20, "bold"))
        self.goto(0, 0)
        self.write("5", move=False, align="center", font=("Arial", 20, "bold"))
        self.goto(WIDTH*2/3, 0)
        self.write("6", move=False, align="center", font=("Arial", 20, "bold"))
        self.goto(-WIDTH*2/3, -HEIGHT*2/3)
        self.write("7", move=False, align="center", font=("Arial", 20, "bold"))
        self.goto(0, -HEIGHT*2/3)
        self.write("8", move=False, align="center", font=("Arial", 20, "bold"))
        self.goto(WIDTH*2/3, -HEIGHT*2/3)
        self.write("9", move=False, align="center", font=("Arial", 20, "bold"))