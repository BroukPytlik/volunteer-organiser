# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0022_auto_20150727_2138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='volunteer',
            name='pid',
            field=models.IntegerField(verbose_name='PID', default=1, blank=True),
            preserve_default=False,
        ),
    ]
