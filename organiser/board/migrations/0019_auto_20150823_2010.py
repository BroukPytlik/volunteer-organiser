# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0018_duty_recurent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duty',
            name='recurent',
        ),
        migrations.AddField(
            model_name='duty',
            name='recurrent',
            field=models.BooleanField(verbose_name='recurrent', default=False),
        ),
        migrations.AlterField(
            model_name='duty',
            name='date',
            field=models.DateField(help_text='If the duty is recurrent, then this will be its first day, and the duty will repeat weekly.', verbose_name='date'),
        ),
    ]
