# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0020_auto_20150727_2053'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ward',
            new_name='Category',
        ),
        migrations.RemoveField(
            model_name='duty',
            name='ward',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='availableWards',
        ),
        migrations.AddField(
            model_name='duty',
            name='category',
            field=models.ForeignKey(default=0, to='board.Category', verbose_name='category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='availableCategories',
            field=models.ManyToManyField(to='board.Category', verbose_name='available categories'),
        ),
    ]
