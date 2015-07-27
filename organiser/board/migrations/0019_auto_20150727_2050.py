# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0018_auto_20150727_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='diagnosis',
            field=models.TextField(verbose_name='diagnosis', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='availableWards',
            field=models.ManyToManyField(to='board.Ward', verbose_name='available wards'),
        ),
    ]
