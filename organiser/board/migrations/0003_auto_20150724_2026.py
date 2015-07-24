# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20150724_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='duty',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='duty',
            name='stopped',
            field=models.DateTimeField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='duty',
            name='recurent',
            field=models.BooleanField(default=False),
        ),
    ]
