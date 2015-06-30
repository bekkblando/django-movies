# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('movieID', models.IntegerField()),
                ('imdbId', models.IntegerField()),
                ('tmdbId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('movieId', models.IntegerField()),
                ('title', models.CharField(max_length=140)),
                ('genres', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('userId', models.CharField(max_length=140)),
                ('movieId', models.CharField(max_length=140)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=7)),
                ('timestamp', models.BigIntegerField()),
            ],
        ),
    ]
