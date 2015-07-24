# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='duty',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 24, 18, 7, 54, 530638, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='duty',
            name='recurent',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ward',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
