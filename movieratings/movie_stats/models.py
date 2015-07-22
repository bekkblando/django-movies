from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import time
# Create your models here.


class Rater(models.Model):
    user_link = models.OneToOneField(User)
    userId = models.IntegerField()
    gender = models.CharField(max_length=1, default=0)
    age = models.IntegerField(default=0)
    occupation = models.CharField(max_length=140, default=0)
    zip = models.CharField(max_length=140, default=0)

    def __str__(self):
        return "User ID: {}, Gender: {}, Age: {}".format(self.userId, self.gender, self.age)

    def movies_rated(self):
        return Review.objects.filter(userId=self)


class ReviewManager(models.Manager):
    def ratemovie(self, userid, movie_id, rate):
        if not self.filter(movieId=Movie.objects.filter(movieId=movie_id), userId=userid):
            reviewinstance = self.create(userId=userid,
                                                   movieId=Movie.objects.get(movieId=movie_id),
                                                   rating=rate, timestamp=int(time.time()))
            print(reviewinstance)
            reviewinstance.save()


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

    objects = ReviewManager()



class AvgmovrateManager(models.Manager):
    def besttoworst(self):
        sets = []
        all_rates = self.order_by('avg_mov').all()
        for item in all_rates:
            if item.avg_mov:
                sets.append(item)
        sets = list(reversed(sets))
        self.order_by('avg_mov')
        return sets[:19]


class Avgmovrate(models.Model):
    movieId = models.ForeignKey(Movie)
    avg_mov = models.DecimalField(max_digits=7, decimal_places=2)


    objects = AvgmovrateManager()

    class Meta:
        ordering = ['avg_mov']

    def __str__(self):
        return "{}, Rating: {} ".format(self.movieId, self.avg_mov)