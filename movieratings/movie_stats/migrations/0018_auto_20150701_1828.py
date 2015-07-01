# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
from django.db import models, migrations
from movie_stats.models import Rater, Movie, Review, Avgmovrate

def getavgrate(x, y):
    # all_rates = Review.objects.all()
    #movrate = [(item.movieId.movieId,Review.objects.filter(movieId = item.movieId)) for item in all_rates]
    """for item in all_rates:
        item.movieId.movieId
        mov_list = []
        for movie in Review.objects.filter(movieId = item.movieId):
            mov_list.append(movie.rating)
        avg_mov = np.mean(mov_list)
        avg_save = Avgmovrate.objects.create(movieId=Movie.objects.get(movieId=item.movieId.movieId), avg_mov=avg_mov)
        print(avg_save)
        avg_save.save()"""
    all_movies = Movie.objects.all()
    for item in all_movies:
        movrate = []
        print("Movie", item)
        for review in Review.objects.filter(movieId = item):
            movrate.append(review.rating)
            #print(item)
        avg_rate = np.mean(movrate)
        if not movrate:
            avg_rate = 0
        print(avg_rate)
        avg_save = Avgmovrate.objects.create(movieId=Movie.objects.get(movieId = item.movieId), avg_mov=avg_rate)
        avg_save.save()




class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0017_avgmovrate'),
    ]

    operations = [
          migrations.RunPython(getavgrate),
    ]
