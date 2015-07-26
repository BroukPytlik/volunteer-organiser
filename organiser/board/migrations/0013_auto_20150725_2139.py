# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_auto_20150724_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birth_day',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='birth_month',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
