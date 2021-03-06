# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-11 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=255, verbose_name='Monto')),
                ('installments', models.CharField(choices=[(6, 6), (12, 12), (24, 24), (36, 36)], default=6, max_length=2, verbose_name='Cuotas')),
                ('description', models.TextField(blank=True, max_length=1500)),
                ('status', models.CharField(choices=[(0, 'Creada'), (1, 'Evaluada'), (2, 'Aprobada'), (3, 'Rechazada')], default=0, max_length=2, verbose_name='Estado')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('observations', models.TextField(blank=True, max_length=1500)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Client', verbose_name='Cliente')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.TypeCredit', verbose_name='Tipo de credito')),
            ],
        ),
    ]
