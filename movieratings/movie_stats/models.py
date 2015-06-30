from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Links(models.Model):
    movieID = models.IntegerField()
    imdbId = models.IntegerField()
    tmdbId = models.IntegerField()

class Movies(models.Model):
    movieId = models.IntegerField()
    title = models.CharField(max_length=140)
    genres = models.CharField(max_length=140)

class Rater(models.Model):
    userId = models.CharField(max_length=140)
    movieId = models.CharField(max_length=140)
    rating = models.DecimalField(max_digits=5)
    timestamp = models.BigIntegerField()

with open("Macintosh HD/Users/BekkBlando/Documents/github/django-movies/movieratings/movie_stats/links.csv", 'rt') as in_file:
    links = in_file.read()
    linkslist = links.split('\n')
    for item in linkslist:
        links3 = item.split(',')
        print(len(links3))

with open("Macintosh HD/Users/BekkBlando/Documents/github/django-movies/movieratings/movie_stats/movies.csv", 'rt') as in_file1:
    movie = in_file1.read()
    movielist = movie.split("\n")
    for item in movielist:
        movie3 = item.split(',')
        print(len(movie3))

with open("Macintosh HD/Users/BekkBlando/Documents/github/django-movies/movieratings/movie_stats/ratings.csv", 'rt') as in_file2:
    rater = in_file2.read()
    raterlist = rater.split("\n")
    for item in raterlist:
        rater3 = item.split(',')
        print(len(rater3))