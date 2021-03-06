# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cafe', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.CharField(blank=True, max_length=200, null=True)),
                ('event', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('record', models.CharField(blank=True, max_length=200, null=True)),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='date')),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cafe.Member'),
        ),
    ]
