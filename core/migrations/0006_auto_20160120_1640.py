# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160120_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='core.Tag'),
        ),
    ]