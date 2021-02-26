from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(13, 'Harry Pottear', 'J. K. Rowling', '9.3')")
# db.commit()

#------------------------SQLALCHEMY------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.title} - {self.author} - {self.rating}/10'
db.create_all()
#----------------------------------------------------------------
class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditForm(FlaskForm):
    new_rating = StringField('New Rating', validators=[])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    books = db.session.query(Book).all()
    return render_template("index.html", books=books)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(title=form.book_name.data, author=form.book_author.data, rating=form.rating.data)
        db.session.add(new_book)
        db.session.commit()
        books = db.session.query(Book).all()
        return render_template("index.html", books=books)
    return render_template("add.html", form=form)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    books = db.session.query(Book).all()
    if form.validate_on_submit():
        book_to_update = Book.query.get(id)
        book_to_update.rating = form.new_rating.data
        db.session.commit()
        books = db.session.query(Book).all()
        return render_template("index.html", books=books)
    return render_template("edit.html", form=form, books=books, id=id)

if __name__ == "__main__":
    app.run(debug=True)

