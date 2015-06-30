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

with open("") as in_file:
    links = in_file.read()
    links.split('\n')

with open("") as in_file1:
    movie = in_file1.read()
    movie.split("\n")

with open("") as in_file2:
    rater = in_file2.read()
    rater.split("\n")