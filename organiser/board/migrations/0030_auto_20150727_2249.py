# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0029_auto_20150727_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='workedTo',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='workedUntil',
            field=models.DateField(verbose_name='worked until', null=True, blank=True),
        ),
    ]
