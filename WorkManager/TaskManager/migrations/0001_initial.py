# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('client_name', models.CharField(max_length=1000, verbose_name='Client name')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('time_elapsed', models.IntegerField(null=True, blank=True, default=None, verbose_name='Elapsed time')),
                ('importance', models.IntegerField(verbose_name='Importance')),
                ('project', models.ForeignKey(blank=True, default=None, null=True, to='TaskManager.Project', verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('login', models.CharField(max_length=25, verbose_name='Login')),
                ('password', models.CharField(max_length=50, verbose_name='Name')),
                ('phone', models.DateField(null=True, blank=True, max_length=20, default=None, verbose_name='Phone number')),
                ('bdate', models.DateField(null=True, blank=True, default=None, verbose_name='Birthdate')),
                ('last_connection', models.DateTimeField(null=True, blank=True, default=None, verbose_name='Date last connected')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('years_seniority', models.IntegerField(default=0, verbose_name='Seniority')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Create date')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, to='TaskManager.UserProfile', parent_link=True)),
            ],
            bases=('TaskManager.userprofile',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, to='TaskManager.UserProfile', parent_link=True)),
                ('specialization', models.CharField(max_length=50, verbose_name='Specialization')),
            ],
            bases=('TaskManager.userprofile',),
        ),
        migrations.AddField(
            model_name='task',
            name='developer',
            field=models.ForeignKey(to='TaskManager.Developer', verbose_name='User'),
        ),
        migrations.AddField(
            model_name='developer',
            name='supervisor',
            field=models.ForeignKey(to='TaskManager.Supervisor', verbose_name='supervisor'),
        ),
    ]
