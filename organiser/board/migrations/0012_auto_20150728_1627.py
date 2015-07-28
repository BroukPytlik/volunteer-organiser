# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_auto_20150728_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workedhours',
            name='added',
            field=models.DateField(verbose_name='added'),
        ),
    ]
