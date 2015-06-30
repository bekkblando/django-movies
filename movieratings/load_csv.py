__author__ = 'BekkBlando'

from movie_stats.models import User, Movie, Rater

# from .models import Link, Movie, Rater


def load_in(apps, scheme_editor):
    with open("/Users/BekkBlando/Documents/github/django-movies/movieratings/ratings.dat", 'rt') as in_file2:
        rater = in_file2.read()
        raterlist = rater.split("\n")
        for item in raterlist:
            rater4 = item.split('::')
            if len(rater4) == 4:
                raterinstance = Rater.objects.create(userId=rater4[0],movieId=rater4[1],rating=rater4[2],timestamp=rater4[3])
                raterinstance.save()

    with open("/Users/BekkBlando/Documents/github/django-movies/movieratings/users.dat", 'rt') as in_file:
        users = in_file.read()
        userslist = users.split('\n')
        for item in userslist:
            users5 = item.split('::')
            if len(users5) == 5:
                linkinstance = User.objects.create(userId=Rater.objects.get(userId=int(users5[0]))
                                                   , gender=user5[1], age=int(user5[2]),
                                                   occupation=int(user5[3]), zip=int(user5[4]))
                linkinstance.save()

    with open("/Users/BekkBlando/Documents/github/django-movies/movieratings/movies.dat", 'rt') as in_file1:
        movie = in_file1.read()
        movielist = movie.split("\n")
        for item in movielist:
            movie3 = item.split('::')
            if len(movie3) == 3:
                movieinstance = Movie.objects.create(movieId=Rater.objects.get(movieId=movie3[0]),title=movie3[1],genres=movie3[2])
                movieinstance.save()

    raise Exception("Worked")