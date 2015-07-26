# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0015_person_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='birth_day',
        ),
        migrations.RemoveField(
            model_name='person',
            name='birth_month',
        ),
    ]
