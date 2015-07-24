# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20150724_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='stopped',
            field=models.DateField(blank=True),
        ),
    ]
