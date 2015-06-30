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
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.BigIntegerField()

with open("movie_stats/links.csv", 'rt') as in_file:
    links = in_file.read()
    linkslist = links.split('\n')
    test = linkslist[1].split(',')
    print(test)
    testl = Links(movieID=int(test[0]), imdbId=int(test[1]), tmdbId=int(test[2]))
    testl.save()
    """for item in linkslist:
        links3 = item.split(',')
        print(len(links3))
        if len(links3) == 3:
            Links(movieID=links3[0], imdbId=links3[1], tmdbIb=links3[2])"""

with open("movie_stats/movies.csv", 'rt') as in_file1:
    movie = in_file1.read()
    movielist = movie.split("\n")
    movietest = movielist[1].split(',')
    testm = Movies(movieId=movietest[0],title=movietest[1],genres=movietest[2])
    testm.save()
    """for item in movielist:
        movie3 = item.split(',')
        print(len(movie3))
        if len(movies3) == 3:
            Movies(movieId=movie3[0],title=movie3[1],genres=movie3[2])"""

with open("movie_stats/ratings.csv", 'rt') as in_file2:
    rater = in_file2.read()
    raterlist = rater.split("\n")
    ratertest = raterlist[1].split(',')
    testr = Rater(userId=ratertest[0],movieId=ratertest[1],rating=ratertest[2],timestamp=ratertest[3])
    testr.save()
    """for item in raterlist:
        rater3 = item.split(',')
        print(len(rater3))
        if len(rater3) == 4:
            Rater(userId=rater[0],movieId=rater[1],rating=rating[2],timestamp=rating[3])"""
