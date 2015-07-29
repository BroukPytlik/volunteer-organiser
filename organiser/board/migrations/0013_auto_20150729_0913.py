# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_auto_20150728_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='workedhours',
            name='category1',
            field=models.ForeignKey(default=2, to='board.Category1', verbose_name='category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workedhours',
            name='category2',
            field=models.ForeignKey(null=True, to='board.Category2', verbose_name='subcategory', blank=True),
        ),
        migrations.AlterField(
            model_name='ward',
            name='name',
            field=models.CharField(verbose_name='name', max_length=200),
        ),
    ]
