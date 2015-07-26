# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_auto_20150725_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 7, 26, 6, 36, 51, 985997, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
