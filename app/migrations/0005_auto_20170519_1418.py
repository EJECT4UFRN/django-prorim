# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170518_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erro',
            name='estadia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='erro', to='app.Estadia', verbose_name='Estadia'),
        ),
    ]