# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0024_auto_20150727_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='work_since',
            field=models.DateField(verbose_name='working since', default=datetime.datetime(2015, 7, 27, 20, 15, 18, 675258, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
