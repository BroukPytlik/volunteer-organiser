# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0015_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category2',
            name='contact',
            field=models.CharField(null=True, verbose_name='contact person', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(verbose_name='attachment', upload_to='./'),
        ),
    ]
