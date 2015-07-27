# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0026_auto_20150727_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='phone',
            new_name='phone1',
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='workingSince',
            field=models.DateField(blank=True, verbose_name='working since'),
        ),
    ]
