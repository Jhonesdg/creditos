# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-11 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('rate', models.FloatField(verbose_name='Tasa')),
            ],
        ),
    ]
