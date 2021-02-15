from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def bold():
        return f"<b>{function()}</b>"
    return bold

def make_emphasis(function):
    def emphasis():
        return f"<em>{function()}</em>"
    return emphasis

def make_underlined(function):
    def underlined():
        return f"<u>{function()}</u>"
    return underlined


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "bye !"

app.run(debug=True)

