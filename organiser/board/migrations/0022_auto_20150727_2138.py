# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0021_auto_20150727_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.TextField(verbose_name='name')),
            ],
            options={
                'verbose_name': 'ward',
                'verbose_name_plural': 'wards',
            },
        ),
        migrations.AddField(
            model_name='patient',
            name='ward',
            field=models.ForeignKey(default=0, to='board.Ward', verbose_name='ward'),
            preserve_default=False,
        ),
    ]
