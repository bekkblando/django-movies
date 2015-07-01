from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response
from movie_stats.models import Rater, Movie, Review

# Create your views here.


def ind_movie(request, movieId):
    try:
        movie = Movie.objects.get(id=movieId)
        context = {"Movie": movie}
        return render_to_response("movie.html", context)
    except:
        return HttpResponseNotFound('Movie\'s not in our data :(')


def top_movies(request):
    try:
        #Go through and get top twenty movies
        movie = Movie.objects.get(id=movieId)
        context = {"Movie": movie}
        return render_to_response("movie.html", context)
    except:
        return HttpResponseNotFound('Movie\'s not in our data :(')


def ind_user(request, userId):
    try:
        user = Rater.objects.get(id=userId)
        context = {"Movie": user}
        return render_to_response("user.html", context)
    except:
        return HttpResponseNotFound('User\'s not in our data :(')
