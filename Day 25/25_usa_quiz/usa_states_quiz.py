from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.setup(725, 491)
screen.bgpic('100_days_of_python\Day 25\\25_usa_quiz\\blank_states_img.gif')

data = pd.read_csv('100_days_of_python\Day 25\\25_usa_quiz\\50_states.csv')
df = pd.DataFrame(data)
states = df['state'].tolist()
print(states)

state = Turtle()
state.hideturtle()
state.penup()
state.speed('fastest')

score = 0
game_on = True
while game_on:
    guess = screen.textinput("Name all of the states", f"You have guessed {score} states.\n{len(states)-score} states left.\nType 'Give Up' to quit.\n\nName a state: ").title()
    if guess in states:
        score += 1
        usa = df[df['state'] == guess]
        state.goto(int(usa['x']), int(usa['y']))
        state.write(f"{guess}", move=False, align="center", font=("Arial", 8, "bold"))
    elif guess == 'Give Up':
        for i in states:
            usa = df[df['state'] == i]
            state.goto(int(usa['x']), int(usa['y']))
            state.write(f"{i}", move=False, align="center", font=("Arial", 8, "bold"))
            game_on = False


screen.exitonclick()