# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0023_auto_20150727_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='pid',
            field=models.IntegerField(verbose_name='PID', blank=True, unique=True),
        ),
    ]
