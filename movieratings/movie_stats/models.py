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
        return "User ID: {}, Gender: {}, Age: {}".format(self.userId, self.gender, self.age)

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

    #@property
    def toptwen():
        rates = []
        all_rates = Review.objects.all()
        #for item in all_rates:
            #rates.append(float(item.rating))
        #sort_rate = sorted(rates)[:19]
        #print(sort_rate)
        #final = [Review.objects.exclude(rating = item) for item in sort_rate[0]]
        final = Review.objects.filter(rating=1.0)
        final = list(final)
        movies = []
        for item in final:
            print(int(item.movieId))
            movies.append(Movie.objects.get(movieId = item.movieId))
        return movies

    def __str__(self):
        return "{}, Rating: {} ".format(self.userId, self.rating)