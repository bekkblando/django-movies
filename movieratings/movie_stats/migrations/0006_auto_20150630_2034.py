# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0005_auto_20150630_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=7)),
                ('timestamp', models.BigIntegerField()),
                ('movieId', models.ForeignKey(to='movie_stats.Movie')),
            ],
        ),
        migrations.RemoveField(
            model_name='rater',
            name='movieId',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='rater',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=1, default='M'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='occupation',
            field=models.IntegerField(default=7777),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='zip',
            field=models.IntegerField(default=29609),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rater',
            name='userId',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='review',
            name='userId',
            field=models.ForeignKey(to='movie_stats.Rater'),
        ),
    ]
