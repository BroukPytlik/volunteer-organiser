# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_auto_20150729_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=250)),
                ('attachment', models.FileField(verbose_name='attachment', upload_to='')),
                ('description', models.TextField(verbose_name='description', blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('volunteer', models.ForeignKey(to='board.Volunteer', verbose_name='volunteer')),
            ],
            options={
                'verbose_name_plural': 'Attachments',
                'verbose_name': 'Attachment',
            },
        ),
    ]
