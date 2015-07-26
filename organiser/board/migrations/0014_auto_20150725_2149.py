# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_auto_20150725_2139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='birthday',
            new_name='birthdate',
        ),
    ]
