# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from movie_stats.models import Rater
from django.contrib.auth.models import User

def linkit(x,y):
    all_raters = Rater.objects.all()
    for raters in all_raters:
        raters.user_link = User.objects.get(username=raters.userId)
        print(raters.user_link)
        raters.save()

class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0024_auto_20150705_1512'),
    ]

    operations = [
        migrations.RunPython(linkit),
    ]
