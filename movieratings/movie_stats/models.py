from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Rater(models.Model):
    userId = models.IntegerField()
    movieId = models.IntegerField()
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.BigIntegerField()

class User(models.Model):
    userId = models.ForeignKey(Rater)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    occupation = models.IntegerField()
    zip = models.IntegerField()

class Movie(models.Model):
    movieId = models.ForeignKey(Rater)
    title = models.CharField(max_length=140)
    genres = models.CharField(max_length=140)
