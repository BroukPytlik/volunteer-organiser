# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_auto_20150724_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duty',
            name='day',
        ),
        migrations.RemoveField(
            model_name='duty',
            name='ended',
        ),
        migrations.AddField(
            model_name='duty',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 24, 19, 24, 11, 718143, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
