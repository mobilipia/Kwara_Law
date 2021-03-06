# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_updates'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('packageid', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('numconcurrency', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccessList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField(default=0)),
                ('accesstype', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroupList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('groupid', models.IntegerField(default=0)),
                ('uid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserValidity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField(default=0)),
                ('lastrenewdate', models.DateTimeField(verbose_name='')),
                ('nextrenewdate', models.DateTimeField(verbose_name='')),
            ],
        ),
    ]
