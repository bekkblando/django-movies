# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0009_auto_20150630_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.CharField(max_length=140),
        ),
    ]
