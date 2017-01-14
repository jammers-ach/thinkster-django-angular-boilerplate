# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankimporter', '0004_realtransaction_main_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagLookup',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankimporter.Tag')),
            ],
        ),
    ]
