# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0019_auto_20150727_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='patient',
            field=models.ForeignKey(null=True, blank=True, to='board.Patient', verbose_name='patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='diagnosis',
            field=models.TextField(null=True, blank=True, verbose_name='diagnosis'),
        ),
    ]
