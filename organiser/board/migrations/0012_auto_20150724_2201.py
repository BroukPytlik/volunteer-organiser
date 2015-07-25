# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_auto_20150724_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='ward',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
