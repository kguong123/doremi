# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_remove_recipescrap_recipefk'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeVisitorsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todaycount', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name='Date')),
            ],
        ),
    ]
