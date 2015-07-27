# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'verbose_name': 'category1',
            },
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(null=True, auto_now_add=True, verbose_name='created')),
                ('time', models.IntegerField(default=0, choices=[(0, 'Morning'), (1, 'Afternoon')], verbose_name='time')),
                ('date', models.DateField(verbose_name='date')),
                ('notes', models.TextField(null=True, verbose_name='notes', blank=True)),
                ('category1', models.ForeignKey(to='board.Category', verbose_name='category')),
            ],
            options={
                'verbose_name_plural': 'duties',
                'verbose_name': 'duty',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='first name')),
                ('surname', models.CharField(max_length=20, verbose_name='surname')),
                ('birthdate', models.DateField(verbose_name='birth date')),
                ('birthday', models.DateField()),
                ('notes', models.TextField(null=True, verbose_name='notes', blank=True)),
                ('phone1', models.CharField(max_length=20, null=True, verbose_name='phone', blank=True)),
                ('phone2', models.CharField(max_length=20, null=True, verbose_name='phone', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='e-mail', blank=True)),
                ('address', models.TextField(null=True, verbose_name='address', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.TextField(verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'wards',
                'verbose_name': 'ward',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, to='board.Person', serialize=False, parent_link=True, primary_key=True)),
                ('diagnosis', models.TextField(null=True, verbose_name='diagnosis', blank=True)),
                ('ward', models.ForeignKey(to='board.Ward', verbose_name='ward')),
            ],
            options={
                'verbose_name_plural': 'patients',
                'verbose_name': 'patient',
            },
            bases=('board.person',),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, to='board.Person', serialize=False, parent_link=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('pid', models.IntegerField(unique=True, verbose_name='PID', blank=True)),
                ('workingSince', models.DateField(verbose_name='working since', blank=True)),
                ('workedUntil', models.DateField(null=True, verbose_name='worked until', blank=True)),
                ('professions', models.CharField(max_length=250, null=True, verbose_name='professions', blank=True)),
                ('availableCategories', models.ManyToManyField(to='board.Category', verbose_name='available categories')),
            ],
            options={
                'verbose_name_plural': 'volunteers',
                'verbose_name': 'volunteer',
            },
            bases=('board.person',),
        ),
        migrations.AddField(
            model_name='duty',
            name='patient',
            field=models.ForeignKey(null=True, to='board.Patient', verbose_name='patient', blank=True),
        ),
        migrations.AddField(
            model_name='duty',
            name='volunteer',
            field=models.ForeignKey(to='board.Volunteer', verbose_name='volunteer'),
        ),
    ]
