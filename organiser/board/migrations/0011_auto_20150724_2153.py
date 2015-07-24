# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_auto_20150724_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='ward',
            field=models.ForeignKey(to='board.Ward', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='duty',
            name='time',
            field=models.IntegerField(choices=[(0, 'Morning'), (1, 'Afternoon')], default=0),
        ),
    ]
