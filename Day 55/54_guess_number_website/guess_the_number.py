from flask import Flask
app = Flask(__name__)
import random

correct_number = random.randint(0,9)

@app.route('/')
def say_bye():
    return "<h1>Guess a number between 0 and 9</h1> \n <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/<int:correct_num>')
def correct(correct_num):
    global correct_number
    if correct_num == correct_number:
        return "<h1>YOU GOT IT!</h1>\n<img src='https://media.giphy.com/media/l0IulcCkeqPJIYDTi/giphy.gif'>"
    else:
        return "<h1>YOU FAILED!</h1>\n<img src='https://media.giphy.com/media/3o7ZeCHGCq8vJgj4GY/giphy.gif'>"

print(correct_number)
app.run(debug=True)

