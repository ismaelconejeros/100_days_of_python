from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    my_request = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965")
    posts = my_request.json()
    return render_template("index.html", posts= posts)

@app.route("/post/<int:post_num>")
def post(post_num):
    num = post_num
    my_request = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965")
    posts = my_request.json()
    return render_template("post.html", posts = posts, num = num)

if __name__ == "__main__":
    app.run(debug=True)
