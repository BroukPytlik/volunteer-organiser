# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0016_auto_20150804_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='until',
            field=models.DateField(verbose_name='until', blank=True, null=True),
        ),
    ]
