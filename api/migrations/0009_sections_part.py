# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-24 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_email_sms'),
    ]

    operations = [
        migrations.AddField(
            model_name='sections',
            name='part',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
