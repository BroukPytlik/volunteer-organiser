# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_workedhours'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('since', models.DateTimeField(verbose_name='since')),
                ('until', models.DateTimeField(verbose_name='until')),
                ('reason', models.CharField(blank=True, verbose_name='reason', max_length=250, null=True)),
                ('volunteer', models.ForeignKey(to='board.Volunteer', verbose_name='volunteer')),
            ],
            options={
                'verbose_name': 'holiday',
                'verbose_name_plural': 'holidays',
            },
        ),
    ]
