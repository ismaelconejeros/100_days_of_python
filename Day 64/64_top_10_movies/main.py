from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies_db2.db"
db = SQLAlchemy(app)

TMDB_ENDPOINT = 'https://api.themoviedb.org/3/search/movie?'
TMDB_API_KEY = '3ce00399ab3690c4fb1cf9bc3d49ca85'

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.String(80), nullable=False)
    ranking = db.Column(db.String(80), nullable=False)
    review = db.Column(db.String(80), nullable=False)
    img_url = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.title}'
db.create_all()

class EditReview(FlaskForm):
    new_review = StringField('New Review', validators=[DataRequired()])
    new_rating = StringField('New Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddMovie(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    movies = db.session.query(Movie).all()
    form = EditReview()
    if form.validate_on_submit():
        movie_to_update = Movie.query.get(id)
        movie_to_update.review = form.new_review.data
        movie_to_update.rating = form.new_rating.data
        db.session.commit()
        return redirect( url_for("home"))
    return render_template("edit.html", movies=movies, id=id, form=form)

@app.route("/delete/<int:id>")
def delete(id):
    movies = db.session.query(Movie).all()
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect( url_for('home', movies=movies, id=id))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        my_request = requests.get(url=TMDB_ENDPOINT, params={'api_key':TMDB_API_KEY, 'query':form.title.data})
        data = my_request.json()['results']
        return render_template("select.html", options=data)
    return render_template('add.html', form=form) 

@app.route("/select/<int:id>")
def select(id):
    form = EditReview()
    my_request = requests.get(url=f'https://api.themoviedb.org/3/movie/{id}?', params={'api_key':TMDB_API_KEY})
    data = my_request.json()
    new_movie = Movie(
        id = data['id'],
        title=data['title'],
        year=data['release_date'].split('-')[0],
        description=data['overview'],
        rating="",
        ranking=len(db.session.query(Movie).all())+1,
        review="",
        img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))

#test
if __name__ == '__main__':
    app.run(debug=True)
