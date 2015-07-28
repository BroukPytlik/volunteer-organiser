# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20150728_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkedHours',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('added', models.DateTimeField(verbose_name='added')),
                ('hours', models.IntegerField(verbose_name='worked hours')),
                ('volunteer', models.ForeignKey(to='board.Volunteer', verbose_name='volunteer')),
            ],
            options={
                'verbose_name_plural': 'worked hours',
                'verbose_name': 'worked hours',
            },
        ),
    ]
