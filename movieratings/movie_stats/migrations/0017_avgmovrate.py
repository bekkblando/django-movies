# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0016_auto_20150701_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avgmovrate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('avg_mov', models.IntegerField()),
                ('movieId', models.ForeignKey(to='movie_stats.Movie')),
            ],
        ),
    ]
