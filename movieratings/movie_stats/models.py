from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Link(models.Model):
    movieID = models.IntegerField()
    imdbId = models.IntegerField()
    tmdbId = models.IntegerField()

class Movie(models.Model):
    movieId = models.IntegerField()
    title = models.CharField(max_length=140)
    genres = models.CharField(max_length=140)

class Rater(models.Model):
    userId = models.CharField(max_length=140)
    movieId = models.CharField(max_length=140)
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.BigIntegerField()
