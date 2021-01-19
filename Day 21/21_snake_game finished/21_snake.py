import turtle
import random
import time
from snake_classes import Snake, Food, Scoreboard, Margin

screen = turtle.Screen()
screen.screensize(600, 600, "black")
screen.tracer(0)

scoreboard = Scoreboard()
margin = Margin()
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

    if snake.head.distance(food) < 15: #Eat Food
        food.refresh()
        scoreboard.score_up()
        snake.add_new_part()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280: #Crash Wall
        scoreboard.game_over()
        game_on = False

    for i in snake.parts: #Crash Body
        if snake.head.distance(i) < 10 and i in snake.parts[1:]:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()