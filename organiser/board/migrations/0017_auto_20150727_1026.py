# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0016_auto_20150726_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerWard',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='duty',
            options={'verbose_name_plural': 'duties', 'verbose_name': 'duty'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name_plural': 'patients', 'verbose_name': 'patient'},
        ),
        migrations.AlterModelOptions(
            name='volunteer',
            options={'verbose_name_plural': 'volunteers', 'verbose_name': 'volunteer'},
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ward',
        ),
        migrations.AddField(
            model_name='duty',
            name='ward',
            field=models.ForeignKey(default=1, verbose_name='ward', to='board.Ward'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='duty',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='notes',
            field=models.TextField(null=True, blank=True, verbose_name='notes'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='patient',
            field=models.ForeignKey(to='board.Patient', verbose_name='patient'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='time',
            field=models.IntegerField(choices=[(0, 'Morning'), (1, 'Afternoon')], verbose_name='time', default=0),
        ),
        migrations.AlterField(
            model_name='duty',
            name='volunteer',
            field=models.ForeignKey(to='board.Volunteer', verbose_name='volunteer'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthdate',
            field=models.DateField(verbose_name='birth date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(null=True, max_length=254, blank=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(null=True, blank=True, verbose_name='notes'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(null=True, max_length=20, blank=True, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=20, verbose_name='surname'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='active',
            field=models.BooleanField(verbose_name='active', default=True),
        ),
        migrations.AddField(
            model_name='volunteerward',
            name='volunteer',
            field=models.ForeignKey(to='board.Volunteer', verbose_name='volunteer'),
        ),
        migrations.AddField(
            model_name='volunteerward',
            name='ward',
            field=models.ForeignKey(to='board.Ward', verbose_name='ward'),
        ),
    ]
