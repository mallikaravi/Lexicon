# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-05-11 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Third_App', '0002_auto_20220511_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=225, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=225, unique=True),
        ),
    ]
