__author__ = 'BekkBlando'

from movie_stats.models import Link, Movie, Rater
import pandas as pd

# from .models import Link, Movie, Rater


def load_in(apps, scheme_editor):
    users = pd.read_csv('/Users/BekkBlando/Documents/github/django-movies/movieratings/users.dat')#, names=["id", "message", "painting"])
    #splat_df.fillna(0, inplace=True)
    print(users)

    """
    for row in splat_df.iterrows():
    links = in_file.read()
    linkslist = links.split('\n')
    test = linkslist[1].split(',')
    print(test)
    testl = Link(movieID=int(test[0]), imdbId=int(test[1]), tmdbId=int(test[2]))
    testl.save()
    for item in linkslist:
        links3 = item.split(',')
        # print(len(links3))
        if len(links3) == 3 and links3[0].isdigit() and links3[1].isdigit() and links3[2].isdigit():
            # print(links3[0])
            linkinstance = Link.objects.create(movieID=int(links3[0]), imdbId=int(links3[1]), tmdbId=int(links3[2]))
            linkinstance.save()"""

    movies = pd.read_csv('/Users/BekkBlando/Documents/github/django-movies/movieratings/movies.dat')#, names=["id", "message", "painting"])
    #splat_df.fillna(0, inplace=True)
    print(movies.head())
    """#for row in splat_df.iterrows():
        movie = in_file1.read()
        movielist = movie.split("\n")
        # movietest = movielist[1].split(',')
        testm = Movie(movieId=movietest[0], title=movietest[1], genres=movietest[2])
        testm.save()
        for item in movielist:
            movie3 = item.split(',')
            # print(len(movie3))
            if len(movie3) == 3:
                if movie3[0] ==
                movieinstance = Movie.objects.create(movieId=Link.objects.get(movieId=movie3[0]),title=movie3[1],genres=movie3[2])
                movieinstance.save()"""

    raters = pd.read_csv('/Users/BekkBlando/Documents/github/django-movies/movieratings/ratings.dat')#, names=["id", "message", "painting"])
    #splat_df.fillna(0, inplace=True)
    print(raters.head())
    """#for row in splat_df.iterrows():
        rater = in_file2.read()
        raterlist = rater.split("\n")
        ratertest = raterlist[1].split(',')
        testr = Rater(userId=ratertest[0], movieId=ratertest[1], rating=ratertest[2], timestamp=ratertest[3])
        testr.save()
        for item in raterlist:
            rater3 = item.split(',')
            print(len(rater3))
            if len(rater3) == 4:
                raterinstance = Rater.objects.create(userId=rater[0],movieId=rater[1],rating=rating[2],timestamp=rating[3])
                raterinstance.save()"""
    raise Exception()