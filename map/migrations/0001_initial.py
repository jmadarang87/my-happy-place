# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-09-27 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField()),
                ('date_landed', models.DateTimeField(blank=True, null=True)),
                ('date_departure', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
