# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from load_csv import load_in

class Migration(migrations.Migration):

    dependencies = [
        ('movie_stats', '0003_auto_20150630_1401'),
    ]

    operations = [
        migrations.RunPython(load_in),
    ]
