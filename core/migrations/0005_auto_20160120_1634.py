# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160120_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='core.Category'),
        ),
    ]