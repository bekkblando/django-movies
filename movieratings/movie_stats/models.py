from django.db import models

# Create your models here.
from django.db import models
import numpy

# Create your models here.

class Rater(models.Model):
    userId = models.IntegerField()
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    occupation = models.CharField(max_length=140)
    zip = models.CharField(max_length=140)

    def __str__(self):
        return "User ID: {}, Gender: {}, Age: {}".format(self.userId, self.gender, self.age)

    def movies_rated(self):
        return Review.objects.filter(userId = self)

class Movie(models.Model):
    movieId = models.IntegerField()
    title = models.CharField(max_length=140)
    genres = models.CharField(max_length=140)


    def __str__(self):
        return "Movie ID: {}, Title: {}, Genres: {}".format(self.movieId, self.title, self.genres)

class Review(models.Model):
    userId = models.ForeignKey(Rater)
    movieId = models.ForeignKey(Movie)
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.BigIntegerField()

    def __str__(self):
        return "{}, Rating: {} ".format(self.movieId, self.rating)

class Avgmovrate(models.Model):
    movieId = models.ForeignKey(Movie)
    avg_mov = models.DecimalField(max_digits=7, decimal_places=2)
    ordering = ['avg_mov']

    def __str__(self):
            return "{}, Rating: {} ".format(self.movieId, self.avg_mov)

    def besttoworst():
        sets = []
        all_rates = Avgmovrate.objects.order_by('avg_mov').all()
        for item in all_rates:
            if item.avg_mov:
                sets.append(item)
        sets = list(reversed(sets))
        #Avgmovrate.objects.order_by('avg_mov')
        return sets[:19]