# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='supervisor',
            field=models.ForeignKey(to='TaskManager.Supervisor', verbose_name='Supervisor'),
        ),
        migrations.RemoveField(
            model_name='task',
            name='developer',
        ),
        migrations.AddField(
            model_name='task',
            name='developer',
            field=models.ManyToManyField(to='TaskManager.Developer'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=50, verbose_name='Password'),
        ),
    ]
