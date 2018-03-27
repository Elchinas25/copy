# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votations', '0002_votation_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average', models.FloatField(default=5)),
            ],
        ),
    ]
