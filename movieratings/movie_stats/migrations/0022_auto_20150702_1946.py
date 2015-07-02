# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
from django.db import models, migrations
from movie_stats.models import Rater, Movie, Review, Avgmovrate

def getavgrate(x, y):
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
        ('movie_stats', '0021_auto_20150702_1945'),
    ]

    operations = [
        migrations.RunPython(getavgrate),
    ]
