# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankimporter', '0002_auto_20170107_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='realtransaction',
            name='date',
            field=models.DateField(default='2016-01-01'),
        ),
        migrations.AddField(
            model_name='realtransaction',
            name='payment_type',
            field=models.CharField(default='card', max_length=20),
        ),
        migrations.AddField(
            model_name='realtransaction',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='realtransaction',
            name='tags',
            field=models.ManyToManyField(to='bankimporter.Tag'),
        ),
    ]