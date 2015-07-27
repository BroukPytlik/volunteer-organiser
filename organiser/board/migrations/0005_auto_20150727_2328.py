# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20150727_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='category2',
            field=models.ForeignKey(null=True, to='board.Category2', blank=True, verbose_name='subcategory'),
        ),
    ]
