# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from movie_stats.models import Rater

def test(x,y):
    for rater in Rater.objects.all():
        print(str(rater.userId)+"password'")
    raise Exception()
class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0023_rater_user_link'),
    ]

    operations = [
        migrations.RunPython(test),
    ]
