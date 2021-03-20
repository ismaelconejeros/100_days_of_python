from turtle import Turtle, Screen
import random

#Create screen
screen = Screen()                                
screen.bgcolor("black")                                
screen.title("Space invaders")

#Create the Borders
class Borders(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.speed(0)
        self.color("white")
        self.penup()
        self.setposition(-300,-300)
        self.pendown()
        self.pensize(3)
        for side in range(4):
            self.fd(600)
            self.lt(90)
            self.hideturtle()

#Create the player
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("turtle")
        self.penup()
        self.speed(0)
        self.setposition(0,-250)
        self.setheading(90)
        self.steps = 15

    def move_left(self):
        x = self.xcor()
        x -= self.steps
        if x < -280:
            x=-280
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += self.steps
        if x > 280:
            x = 280
        self.setx(x)

#Create the Enemy
class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.steps = 15
        self.exists = True

#Create the bullet
class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(0.5,0.5)
        self.hideturtle()
        self.bulletspeed = 10
        self.state = "not_fired"

#Create Scoreboard
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setposition(-250, 270)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 18, "bold"))

    def score_up(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 18, "bold"))


#Objects
player = Player()
bullet = Bullet()
borders = Borders()
scoreboard = ScoreBoard()
number_of_enemies = 10
enemies = []
for i in range(number_of_enemies):
    new_enemy = Enemy()
    enemies.append(new_enemy)
for enemy in enemies:
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

def fire_bullet():
    global number_of_enemies
    if bullet.state == "not_fired":
        bullet.state = "fired"
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()
        for i in range(100):
            bullet.forward(bullet.bulletspeed)
            for enemy in enemies:
                if bullet.distance(enemy) < 10 and enemy.exists:
                    scoreboard.score_up()
                    enemy.exists = False
                    enemy.hideturtle()
                    if scoreboard.score % number_of_enemies == 0:
                        number_of_enemies += 10
                        for i in range(number_of_enemies):
                            new_enemy = Enemy()
                            enemies.append(new_enemy)
                        for enemy in enemies:
                            x = random.randint(-200,200)
                            y = random.randint(100,250)
                            enemy.setposition(x,y)
                    break
        bullet.hideturtle()
        bullet.state = "not_fired"

#Controllers
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkey(fire_bullet, "space")
screen.listen()
game_on = True
while game_on:
    screen.update()

    for enemy in enemies:
        x = enemy.xcor()
        x += enemy.steps
        enemy.setx(x)
        if enemy.xcor() >= 280:
            for enem in enemies:
                y = enem.ycor()
                y -= 10
                enem.sety(y)
                enem.steps *= -1
        if enemy.xcor() <= -280:
            for enem in enemies:
                y = enem.ycor()
                y -= 30
                enem.sety(y)
                enem.steps *= -1
        if enemy.ycor() <= -300:
            enemy.hideturtle()
            enemy.goto(0,0)
            enemy.color('white')
            enemy.write("GAME OVER", move=False, align="center", font=("Arial", 40, "bold"))
            game_on = False

screen.exitonclick()