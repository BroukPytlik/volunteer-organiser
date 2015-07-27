# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0027_auto_20150727_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(null=True, verbose_name='address', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='phone2',
            field=models.CharField(max_length=20, null=True, verbose_name='phone', blank=True),
        ),
    ]
