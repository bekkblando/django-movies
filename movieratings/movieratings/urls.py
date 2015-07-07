"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from movie_stats.views import ind_movie, top_movies, ind_user, index, regis, profile, CreateReviewView, ReviewDelete, wtd
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url('^register/', CreateView.as_view(
            template_name='registration/create_user.html',
            form_class=UserCreationForm,
            success_url='/'), name="regis"),
    url('^rate/', CreateReviewView.as_view(
        template_name='ratemovie.html',
        success_url='profile'), name="rate"),
    url('^delrate<slug>/', ReviewDelete.as_view(
        template_name='deleterating.html',
        success_url='profile'), name="delrate"),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls), name="admin"),
    url(r'^wtd/', wtd, name="wtd"),
    url(r'^movie(?P<movieId>\d+)/$', ind_movie, name="indi_movie"),
    url(r'^profile/$', profile, name="profile"),
    url(r'^toptwenty/', top_movies, name="toptwenty"),
    url(r'^user(?P<userId>\d+)/$', ind_user, name="indi_user"),
    url('^', index),
]
