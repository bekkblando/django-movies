# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0020_auto_20150702_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avgmovrate',
            name='avg_mov',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
