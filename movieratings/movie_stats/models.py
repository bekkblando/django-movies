from django.db import models

# Create your models here.
from django.db import models
import numpy
from django.contrib.auth.models import User
import time
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
# Create your models here.

class Rater(models.Model):
    user_link = models.OneToOneField(User)
    userId = models.IntegerField()
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    occupation = models.CharField(max_length=140)
    zip = models.CharField(max_length=140)


    def __str__(self):
        return "User ID: {}, Gender: {}, Age: {}".format(self.userId, self.gender, self.age)

    def movies_rated(self):
        return Review.objects.filter(userId = self)

    def ratemovie(userid, movie_id, rate):
        print("ran")
        print(userid, movie_id, rate)
        if not Review.objects.filter(movieId = Movie.objects.filter(movieId=movie_id), userId=userid):
            print("ranfully")
            print(int(time.time()))
            reviewinstance = Review.objects.create(userId=userid,
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
        Avgmovrate.objects.order_by('avg_mov')
        return sets[:19]

    #Ignore
    def recommendations(userid):
        print(userid)
        all_rates = []
        final_rates = []
        final_genre = []
        user = Rater.objects.get(userId = userid)
        movies = Review.objects.filter(userId = user).values('movieId')
        for movie in movies:
            for key, value in movie.items():
                print(value)
                try:
                    all_rates.append(Avgmovrate.objects.get(movieId = Movie.objects.filter(movieId=int(value))))
                except:
                    pass
                print(all_rates)
        for item in all_rates:
                print(type(item))
                final_rates.append(float(item.avg_mov))
                final_genre.append(item.movieId.genres)
                final_list = list(zip(final_genre, final_rates))
                #final_rates.append(list(item.avg_mov) + list(item.movieId.genres))
        print(final_rates)

        #pca = PCA(n_components=1)
        #pca.fit(final_list)
        #reduced_movie = pca.transform(final_list)
        kmeans = KMeans(3)
        kmeans.fit(final_list)
        movie_cluster = kmeans.predict(final_list)
        print(movie_cluster)
