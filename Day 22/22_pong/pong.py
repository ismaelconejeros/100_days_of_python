from turtle import Turtle, Screen
import random
from pong_classes import PaddleUser, PaddlePC, Ball, Scoreboard, Margin, WIDTH, HEIGHT

screen = Screen()
screen.setup(1300, 700)
screen.screensize(WIDTH*2, HEIGHT*2, 'black')
screen.tracer(0)

margin = Margin()
scoreboard = Scoreboard()
paddle_user = PaddleUser()
paddle_pc = PaddlePC()
ball = Ball()

screen.listen()
screen.onkeypress(paddle_user.up, "Up")
screen.onkeypress(paddle_user.down, "Down")

game_on = True
while game_on:
    screen.update()
    paddle_user.move()
    paddle_pc.move()
    ball.move()

    for i in range(5):
        if paddle_pc.paddle[i].distance(ball) < 15:
            ball.move_left()
        elif paddle_user.paddle[i].distance(ball) < 15:
            ball.move_right()

    if ball.xcor() > WIDTH+80:
        scoreboard.user_point()
        ball = Ball()
        paddle_pc.go_center()
    if ball.xcor() < -WIDTH-80:
        scoreboard.pc_point()
        ball = Ball()
        paddle_pc.go_center()


screen.exitonclick()