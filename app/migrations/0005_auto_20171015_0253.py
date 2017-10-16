# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-15 05:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170907_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceStatusEstadia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('desativado', models.BooleanField(default=False, verbose_name='Desativado')),
            ],
            options={
                'verbose_name': 'Opção de status para estadias',
                'verbose_name_plural': 'Opção de status para estadias',
            },
        ),
        migrations.CreateModel(
            name='ChoiceStatusManutencaoCorretiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('atualizado', models.DateTimeField(auto_now=True, verbose_name='Última atualização')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('desativado', models.BooleanField(default=False, verbose_name='Desativado')),
            ],
            options={
                'verbose_name': 'Opção de status para manutenção corretiva',
                'verbose_name_plural': 'Opção de status para manutenção corretiva',
            },
        ),
        migrations.AlterModelOptions(
            name='choiceperiodoturno',
            options={'verbose_name': 'Opção de período para sessões', 'verbose_name_plural': 'Opções de período para sessões'},
        ),
        migrations.AlterModelOptions(
            name='secao',
            options={'ordering': ['-data'], 'verbose_name': 'Sessão', 'verbose_name_plural': 'Sessões'},
        ),
        migrations.AlterField(
            model_name='estadia',
            name='secao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estadias', to='app.Secao', verbose_name='Sessão'),
        ),
        migrations.AddField(
            model_name='estadia',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ChoiceStatusEstadia', verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='manutencaocorretiva',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ChoiceStatusManutencaoCorretiva', verbose_name='Status'),
        ),
    ]
