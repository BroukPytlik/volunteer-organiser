# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0019_auto_20150823_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='duty',
            name='normalized_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
