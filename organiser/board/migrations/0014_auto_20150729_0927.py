# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_auto_20150729_0913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='holiday',
            options={'verbose_name': 'Vacancy', 'verbose_name_plural': 'Vacancies'},
        ),
        migrations.AddField(
            model_name='volunteer',
            name='insured',
            field=models.BooleanField(verbose_name='insured', default=False),
        ),
    ]
