# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20170505_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('packageid', models.IntegerField(default=0)),
                ('tablename', models.CharField(max_length=100)),
                ('fulltablename', models.CharField(max_length=100)),
            ],
        ),
    ]
