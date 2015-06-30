__author__ = 'BekkBlando'

from movie_stats.models import Rater, Movie, Review

# from .models import Link, Movie, Rater


def load_in(apps, scheme_editor):
    print("Loaded")
    with open("/Users/BekkBlando/Documents/github/django-movies/movieratings/users.dat", 'rt') as in_file:
        users = in_file.read()
        userslist = users.split('\n')
        for item in userslist:
            users5 = item.split('::')
            #print("RUNNN")
            if len(users5) == 5:
                linkinstance = Rater.objects.create(userId=users5[0], gender=users5[1], age=int(users5[2]),
                                                   occupation=users5[3], zip=users5[4])
                linkinstance.save()
        print("Users Ran")

    with open("/Users/BekkBlando/Documents/github/django-movies/movieratings/movies.dat", 'rt') as in_file1:
        movie = in_file1.read()
        movielist = movie.split("\n")
        for item in movielist:
            movie3 = item.split('::')
            if len(movie3) == 3:
                movieinstance = Movie.objects.create(movieId=movie3[0],title=movie3[1],genres=movie3[2])
                movieinstance.save()

    with open("/Users/BekkBlando/Documents/github/django-movies/movieratings/ratings.dat", 'rt') as in_file2:
        review = in_file2.read()
        raviewlist = review.split("\n")
        for item in raviewlist:
            review4 = item.split('::')
            if len(review4) == 4:
                reviewinstance = Review.objects.create(userId=Rater.objects.get(userId=int(review4[0])),
                                                     movieId=Movie.objects.get(movieId=review4[1]),
                                                       rating=review4[2],timestamp=review4[3])
                reviewinstance.save()

    raise Exception("Worked")