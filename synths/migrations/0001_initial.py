# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Synthesizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]