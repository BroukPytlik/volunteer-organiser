# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_person_cssclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='CssClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('cls', models.CharField(max_length=250, verbose_name='CSS class')),
            ],
            options={
                'verbose_name': 'style',
                'verbose_name_plural': 'styles',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='cssClass',
            field=models.ForeignKey(null=True, blank=True, verbose_name='style', to='board.CssClass'),
        ),
    ]
