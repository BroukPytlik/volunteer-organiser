# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20150724_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duty',
            name='recurent',
        ),
        migrations.AlterField(
            model_name='duty',
            name='time',
            field=models.IntegerField(choices=[(1, 'Morning'), (2, 'Afternoon')], default=1),
        ),
    ]
