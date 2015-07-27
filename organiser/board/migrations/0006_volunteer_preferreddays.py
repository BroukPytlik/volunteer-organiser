# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20150727_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='preferredDays',
            field=models.CharField(blank=True, max_length=250, verbose_name='preferred days', null=True),
        ),
    ]
