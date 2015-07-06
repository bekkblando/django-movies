from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response
from movie_stats.models import Rater, Movie, Review, Avgmovrate, AvgmovrateManager, ReviewManager
from django.template import RequestContext

# Create your views here.


def ind_movie(request, movieId):
    try:
        movie = Movie.objects.get(id=movieId)
        context = {"Movie": movie}
        return render_to_response("movie.html", context)
    except:
        return HttpResponseNotFound('Movie\'s not in our data :(')


def top_movies(request):
    #Go through and get top twenty movies
    all_rates = AvgmovrateManager.besttoworst()
    #movie = Movie.objects.get(id=movieId)
    context = {"all": all_rates}
    return render_to_response("toptwentymovies.html", context)
    """except:
    return HttpResponseNotFound('Movie\'s not in our data :(')"""

def profile(request):
    print(request.user.username)
    #Avgmovrate.recommendations(request.user.username)
    if request.POST:
        print(request.POST)
        movieId = request.POST['movie']
        rate = request.POST['rate']
        print(movieId, rate)
        ReviewManager.ratemovie(Rater.objects.get(userId=request.user.username), movieId, rate)
    try:
        user = Rater.objects.get(id=request.user.username)
        context = {"user": user, "movies_watched": user.movies_rated()}
        return render_to_response("profile.html", context, context_instance=RequestContext(request))
    except:
        return HttpResponseNotFound('User\'s not in our data :(')


def ind_user(request, userId):
    try:
        user = Rater.objects.get(id=userId)
        context = {"user": user, "movies_watched": user.movies_rated()}
        return render_to_response("user.html", context)
    except:
        return HttpResponseNotFound('User\'s not in our data :(')

def index(request):
    return render_to_response("index.html")

def regis(request):
    return render_to_response("create_user.html")