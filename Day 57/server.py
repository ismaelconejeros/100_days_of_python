from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

def get_age(name):
    my_request = requests.get(url="https://api.agify.io?", params={"name":name})
    age = my_request.json()["age"]
    return age
def get_gender(name):
    my_request = requests.get(url="https://api.genderize.io?", params={"name":name})
    gender = my_request.json()["gender"]
    return gender

@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().strftime("%Y")
    return render_template(
        "index.html", 
        num=random_number, 
        current_year=current_year
        )

@app.route("/guess/<name>")
def guess(name):
    name_1 = name.title()
    return render_template(
        "guess.html",
        name=name_1,
        age=get_age(name_1),
        gender=get_gender(name_1)
    )

@app.route("/blog/<num>")
def blog(num):
    my_request = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965")
    data = my_request.json()
    return render_template(
        "blog.html",
        posts=data
    )

if __name__ == "__main__":
    app.run(debug=True)