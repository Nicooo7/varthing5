# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-30 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revendication', '0013_auto_20170323_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='lieu',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
