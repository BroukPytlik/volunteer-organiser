# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('time', models.TimeField()),
                ('day', models.CharField(default='0', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('notes', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('person_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, to='board.Person', parent_link=True)),
                ('ward', models.ForeignKey(to='board.Ward')),
            ],
            bases=('board.person',),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('person_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, to='board.Person', parent_link=True)),
            ],
            bases=('board.person',),
        ),
        migrations.AddField(
            model_name='duty',
            name='patient',
            field=models.ForeignKey(to='board.Patient'),
        ),
        migrations.AddField(
            model_name='duty',
            name='volunteer',
            field=models.ForeignKey(to='board.Volunteer'),
        ),
    ]
