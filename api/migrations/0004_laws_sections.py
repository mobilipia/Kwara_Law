# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-08 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170208_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laws',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('number', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('postdate', models.DateTimeField(verbose_name='post date')),
                ('updatedate', models.DateTimeField(verbose_name='update date')),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lawid', models.IntegerField(default=0)),
                ('partschedule', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=1000)),
                ('body', models.TextField(default='')),
                ('postdate', models.DateTimeField(verbose_name='post date')),
                ('updatedate', models.DateTimeField(verbose_name='update date')),
            ],
        ),
    ]
