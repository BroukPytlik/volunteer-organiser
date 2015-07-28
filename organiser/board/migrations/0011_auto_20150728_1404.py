# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_holiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='since',
            field=models.DateField(verbose_name='since'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='until',
            field=models.DateField(verbose_name='until'),
        ),
    ]
