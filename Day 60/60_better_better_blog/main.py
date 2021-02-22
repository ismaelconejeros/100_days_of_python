from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    contactme_msg = "Contact ME"
    return render_template("contact.html", contactme_msg=contactme_msg)

@app.route("/contact", methods=["POST"])
def form_entry():
    data = request.form
    print(data)

    my_email = "test.for.smtplib90@gmail.com"
    my_password = "smtplibtest01"
    to_adress = "isma.conejeros@gmail.com"

    msg_subject = f"Message from: {data['name_form']}"
    msg_body = f'name: {data["name_form"]} \nemail: {data["email_form"]}\nphone: {data["phone_form"]}\n\ntext: {data["text_form"]}'
    my_msg = f"Subject: {msg_subject}\n\n{msg_body}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=to_adress, 
            msg=my_msg
            )

    contactme_msg = "MESSAGE SENT"
    return render_template("contact.html", contactme_msg=contactme_msg)


if __name__ == "__main__":
    app.run(debug=True)
