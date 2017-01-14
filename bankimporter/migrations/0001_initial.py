# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entry Date', models.DateField()),
                ('Value Date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('kind', models.IntegerField()),
                ('explanation', models.CharField(max_length=20)),
                ('Payer/Payee', models.CharField(blank=True, max_length=20, null=True)),
                ('acc_no', models.CharField(blank=True, max_length=20, null=True)),
                ('reference', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('filling_code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RealTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bankimporter.RawTransaction')),
            ],
        ),
    ]