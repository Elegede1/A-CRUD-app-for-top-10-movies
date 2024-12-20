from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, URL
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap5(app)

# CREATE DB
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    rating = FloatField("Rating", validators=[DataRequired()])
    ranking = IntegerField("Ranking", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    submit = SubmitField("Add Movie")





# CREATE TABLE
# db.create_all()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.ranking.desc()).all()
    return render_template("index.html", movies=movies)

@app.route("/add/", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if request.method == "POST":
        new_movie = Movie(
            title=form.title.data,
            year=form.year.data,
            description=form.description.data,
            rating=form.rating.data,
            ranking=form.ranking.data,
            review=form.review.data,
            img_url=form.img_url.data,
            # title=request.form.get("title"),
            # year=request.form.get("year"),
            # description=request.form.get("description"),
            # rating=request.form.get("rating"),
            # ranking=request.form.get("ranking"),
            # review=request.form.get("review"),
            # img_url=request.form.get("img_url"),
        )
        db.session.add(new_movie)
        db.session.commit()
        flash("Movie added successfully")
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    movie = Movie.query.get(id)
    form = AddMovieForm(
        title=movie.title,
        year=movie.year,
        description=movie.description,
        rating=movie.rating,
        ranking=movie.ranking,
        review=movie.review,
        img_url=movie.img_url,
    )
    if request.method == "POST":
        movie.title = form.title.data
        movie.year = form.year.data
        movie.description = form.description.data
        movie.rating = form.rating.data
        movie.ranking = form.ranking.data
        movie.review = form.review.data
        movie.img_url = form.img_url.data
        db.session.commit()
        flash("Movie updated successfully")
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete/<int:id>")
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    flash("Movie deleted successfully")
    return redirect(url_for("home"))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
