from flask import Flask, render_template, request
app = Flask(__name__)
app.secret_key = "isma"

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class MyForm(FlaskForm):
    name = StringField(label='name', validators=[Email(message="@ and .com")])
    password = PasswordField(label='password', validators=[Length(min=8)])
    submit = SubmitField(label="Log In")

CORRECT_USER = 'admin@email.com'
CORRECT_PASS = '12345678'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.name.data == CORRECT_USER and form.password.data == CORRECT_PASS:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)