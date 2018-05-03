# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-29 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField(default=0)),
                ('accttype', models.IntegerField(default=0)),
                ('lastrenewaldate', models.DateTimeField(verbose_name='last date renewed')),
                ('nextrenewaldate', models.DateTimeField(verbose_name='next date renewed')),
                ('createdate', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('validity', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
                ('secret', models.CharField(max_length=200)),
                ('role', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('createdate', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='AdminRole',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('createdate', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Annotations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField(default=0)),
                ('case_id', models.IntegerField(default=0)),
                ('ratio_title', models.TextField(default='')),
                ('ratio_body', models.TextField(default='')),
                ('position', models.IntegerField(default=0)),
                ('comment', models.TextField(default='')),
                ('createdate', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(default='')),
                ('title', models.TextField(default='')),
                ('suit_number', models.TextField(default='')),
                ('client', models.TextField(default='')),
                ('judges', models.TextField(default='')),
                ('court', models.TextField(default='')),
                ('subject', models.TextField(default='')),
                ('facts', models.TextField(default='')),
                ('commenced', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('iconurl', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stateid', models.IntegerField(default=0)),
                ('countryid', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(default='')),
                ('phone', models.TextField(default='')),
                ('email', models.TextField(default='')),
                ('address', models.TextField(default='')),
                ('facetime', models.TextField(default='')),
                ('skype', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(default='')),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Judgements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('summaryid', models.IntegerField(default=0)),
                ('judgement', models.TextField(default='')),
                ('counsel', models.TextField(default='')),
                ('category_tags', models.TextField(default='')),
                ('date_posted', models.DateTimeField(verbose_name='date posted')),
                ('date_updated', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
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
            name='Maxims',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField(default=0)),
                ('case_id', models.IntegerField(default=0)),
                ('ratio_title', models.TextField(default='')),
                ('ratio_body', models.TextField(default='')),
                ('position', models.IntegerField(default=0)),
                ('comment', models.TextField(default='')),
                ('createdate', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Precedence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=1000)),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Principles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subjectid', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField(default=0)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=25)),
                ('skype', models.CharField(max_length=200)),
                ('facetime', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.IntegerField(default=0)),
                ('city_other', models.CharField(max_length=200)),
                ('state', models.IntegerField(default=0)),
                ('state_other', models.CharField(max_length=200)),
                ('town', models.IntegerField(default=0)),
                ('town_other', models.CharField(max_length=200)),
                ('country', models.IntegerField(default=0)),
                ('createdate', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Ratio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ratio_title', models.CharField(max_length=500)),
                ('ratio_body', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('resourcename', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('createdate', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=500)),
                ('section', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField(max_length=500)),
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
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('countryid', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('catid', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('iconurl', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('principleid', models.IntegerField(default=0)),
                ('caseid', models.IntegerField(default=0)),
                ('case_title', models.CharField(max_length=1000)),
                ('area_of_law', models.CharField(max_length=1000)),
                ('summary_of_facts', models.TextField(default='')),
                ('held', models.TextField(default='')),
                ('issue', models.TextField(default='')),
                ('ratio', models.TextField(default='')),
                ('cases_cited', models.TextField(default='')),
                ('statutes_cited', models.TextField(default='')),
                ('subject_matter', models.TextField(default='')),
                ('courts', models.TextField(default='')),
                ('judgement_date', models.TextField(default='')),
                ('l_citation', models.TextField(default='')),
                ('o_citations', models.TextField(default='')),
                ('sitting_at', models.TextField(default='')),
                ('suit_number', models.CharField(max_length=1000)),
                ('coram', models.TextField(default='')),
                ('party_a_type', models.CharField(max_length=1000)),
                ('party_a_names', models.TextField(default='')),
                ('party_b_type', models.CharField(max_length=1000)),
                ('party_b_names', models.TextField(default='')),
                ('date', models.DateTimeField(verbose_name='date created')),
                ('category_tags', models.CharField(max_length=1000)),
                ('date_posted', models.DateTimeField(verbose_name='date posted')),
                ('date_updated', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('assignee', models.CharField(max_length=500)),
                ('description', models.TextField(default='')),
                ('due', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=500)),
                ('completed', models.CharField(max_length=500)),
                ('case_title', models.TextField(default='')),
                ('notes', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=500)),
                ('secret', models.CharField(max_length=500)),
                ('status', models.IntegerField(default=0)),
                ('is2faverified', models.IntegerField(default=0)),
                ('isemailverified', models.IntegerField(default=0)),
                ('role', models.IntegerField(default=0)),
                ('createdate', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
