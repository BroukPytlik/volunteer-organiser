# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20150727_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='availableSubcategories',
            field=models.ManyToManyField(verbose_name='available subcategories', blank=True, to='board.Category2'),
        ),
    ]
