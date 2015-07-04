# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from movie_stats.models import Rater
from django.contrib.auth.models import User

def setusersrate(x, y):
    for rater in Rater.objects.all():
        rater.user_link = User.objects.create_user(rater.userId, str(rater.userId)+'@gmail.com', str(rater.userId)+"password'")

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie_stats', '0022_auto_20150702_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='user_link',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=False,
        ),

        migrations.RunPython(setusersrate),
    ]
