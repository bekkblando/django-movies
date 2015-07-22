from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response
from django.views.generic import CreateView, DeleteView, UpdateView
from movie_stats.models import Rater, Movie, Review, Avgmovrate, AvgmovrateManager, ReviewManager
from django.template import RequestContext
import time

# Create your views here.


def ind_movie(request, movieId):
    try:
        movie = Movie.objects.get(id=movieId)
        context = {"Movie": movie}
        return render_to_response("movie.html", context)
    except:
        return HttpResponseNotFound('Movie\'s not in our data :(')


def top_movies(request):
    # Go through and get top twenty movies
    all_rates = Avgmovrate.objects.besttoworst()
    # movie = Movie.objects.get(id=movieId)
    context = {"all": all_rates}
    return render_to_response("toptwentymovies.html", context)


def profile(request):
    print(request.user.username)
    try:
        user = Rater.objects.get(user_link=request.user)
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

def wtd(request):
    print(request.user.username)
    #try:
    user = Rater.objects.get(id=request.user.username)
    context = {"user": user, "movies_watched": user.movies_rated()}
    return render_to_response("wtd.html", context, context_instance=RequestContext(request))

def wtupdate(request):
    print(request.user.username)
    #try:
    user = Rater.objects.get(id=request.user.username)
    context = {"user": user, "movies_watched": user.movies_rated()}
    return render_to_response("wtupdate.html", context, context_instance=RequestContext(request))


class CreateReviewView(CreateView):
    model = Review
    template_name = "ratemovie.html"
    success_url = "profile.html"
    fields = ["movieId", "rating"]

    def form_valid(self, form):
        print("Test")
        print(self.request.user)
        rater_user = Rater.objects.get(user_link=self.request.user)
        form.instance.userId = rater_user
        form.instance.timestamp = time.time()
        return super().form_valid(form)

class ReviewDelete(DeleteView):
    model = Review
    success_url = reverse_lazy('profile')

class ReviewUpdate(UpdateView):
    model = Review
    fields = ['rating']
    template_name = 'review_update.html'