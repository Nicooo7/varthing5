# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-30 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revendication', '0016_auto_20170430_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='interets',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='sexe',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
