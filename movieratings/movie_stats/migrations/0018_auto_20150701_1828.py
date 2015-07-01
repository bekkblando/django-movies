# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from movie_stats.models import Rater, Movie, Review, Avgmovrate

def getavgrate():
    all_rates = Review.objects.all()
    #movrate = [(item.movieId.movieId,Review.objects.filter(movieId = item.movieId)) for item in all_rates]
    movrate = []
    for item in all_rates:
        item.movieId.movieId
        mov_list = []
        for movie in Review.objects.filter(movieId = item.movieId):
            mov_list.append(movie.rating)
        avg_mov = numpy.mean(mov_list)
        Avgmovrate.objects.create(movieId=Movie.objects.get(movieId=item.movieId), avg_mov=avg_mov)

class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0017_avgmovrate'),
    ]

    operations = [
          migrations.RunPython(getavgrate),
    ]
