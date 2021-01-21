from turtle import Turtle, Screen
from crossing_classes import WIDTH, HEIGHT, Map, Chicken, Scoreboard, Cars

image = "chicken.gif"
screen = Screen()
screen.setup(WIDTH*2, HEIGHT*2)
screen.bgcolor('lightgray')
screen.tracer(0)
screen.addshape(image)


print(screen.getshapes())

streets = Map()
scoreboard = Scoreboard()
chicken = Chicken()
chicken.shape(image)
cars = Cars()

screen.listen()
screen.onkeypress(chicken.move_up, 'Up')
screen.onkeypress(chicken.move_down, 'Down')
screen.onkeypress(chicken.move_left, 'Left')
screen.onkeypress(chicken.move_right, 'Right')

game_on = True
while game_on:
    screen.update()
    cars.move()

    if chicken.ycor() >= HEIGHT:
        scoreboard.update_score()
        if scoreboard.stage % 5 == 0:
            cars.create_cars()
        chicken.new_level()
        cars.car_levelup()

    for car in cars.cars:
        if chicken.distance(car) < 30:
            scoreboard.game_over()
            game_on = False



screen.exitonclick()