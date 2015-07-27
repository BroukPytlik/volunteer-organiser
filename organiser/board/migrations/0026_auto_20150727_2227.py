# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0025_volunteer_work_since'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='work_since',
            new_name='workingSince',
        ),
    ]
