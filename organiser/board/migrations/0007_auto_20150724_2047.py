# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20150724_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='duty',
            name='day',
            field=models.CharField(default=1, choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], max_length=1),
        ),
        migrations.AlterField(
            model_name='duty',
            name='ended',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='duty',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(null=True, blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(null=True, blank=True, max_length=20),
        ),
    ]
