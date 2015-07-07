# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0026_auto_20150707_0249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avgmovrate',
            options={'ordering': ['avg_mov']},
        ),
        migrations.AlterField(
            model_name='rater',
            name='user_link',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
