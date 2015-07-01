from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Rater(models.Model):
    userId = models.IntegerField()
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    occupation = models.CharField(max_length=140)
    zip = models.CharField(max_length=140)

    def __str__(self):
        return Rater.userId, Rater.gender, Rater.age

class Movie(models.Model):
    movieId = models.IntegerField()
    title = models.CharField(max_length=140)
    genres = models.CharField(max_length=140)

class Review(models.Model):
    userId = models.ForeignKey(Rater)
    movieId = models.ForeignKey(Movie)
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.BigIntegerField()