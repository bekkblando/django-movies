# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0004_auto_20150630_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('userId', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
                ('occupation', models.IntegerField()),
                ('zip', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.AlterField(
            model_name='rater',
            name='movieId',
            field=models.ForeignKey(to='movie_stats.Movie'),
        ),
        migrations.AlterField(
            model_name='rater',
            name='userId',
            field=models.ForeignKey(to='movie_stats.User'),
        ),
    ]
