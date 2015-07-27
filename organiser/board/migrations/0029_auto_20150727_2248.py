# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0028_auto_20150727_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='professions',
            field=models.CharField(max_length=250, blank=True, verbose_name='professions', null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='workedTo',
            field=models.DateField(blank=True, verbose_name='worked to', null=True),
        ),
    ]
