# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_volunteer_preferreddays'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='cssClass',
            field=models.CharField(null=True, max_length=250, verbose_name='style', blank=True),
        ),
    ]
