# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20150724_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='duty',
            old_name='stopped',
            new_name='ended',
        ),
    ]
