# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from movie_stats.models import Avgmovrate

def delete_everything(x, y):
    Avgmovrate.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0018_auto_20150701_1828'),
    ]

    operations = [
        migrations.RunPython(delete_everything),
    ]
