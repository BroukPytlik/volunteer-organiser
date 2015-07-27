# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20150727_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'subcategories',
            },
        ),
        migrations.AlterModelOptions(
            name='category1',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='duty',
            name='category2',
            field=models.ForeignKey(verbose_name='subcategory', to='board.Category2', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='availableSubcategories',
            field=models.ManyToManyField(to='board.Category2', verbose_name='available subcategories'),
        ),
    ]
