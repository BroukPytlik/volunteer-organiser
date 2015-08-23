# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0017_auto_20150804_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='duty',
            name='recurent',
            field=models.BooleanField(default=False, verbose_name='recurent'),
        ),
    ]
