# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0017_auto_20150727_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerward',
            name='volunteer',
        ),
        migrations.RemoveField(
            model_name='volunteerward',
            name='ward',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='availableWards',
            field=models.ManyToManyField(to='board.Ward'),
        ),
        migrations.DeleteModel(
            name='VolunteerWard',
        ),
    ]
