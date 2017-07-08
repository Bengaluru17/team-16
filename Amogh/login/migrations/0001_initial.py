# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-08 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(default='qwerty', max_length=100)),
                ('isAdmin', models.BooleanField()),
                ('score', models.IntegerField()),
                ('level', models.IntegerField()),
                ('test2', models.IntegerField()),
                ('test3', models.IntegerField()),
                ('test4', models.IntegerField()),
                ('test5', models.IntegerField()),
                ('test6', models.IntegerField()),
                ('test7', models.IntegerField()),
                ('test8', models.IntegerField()),
                ('test9', models.IntegerField()),
                ('test10', models.IntegerField()),
                ('test', models.IntegerField()),
            ],
        ),
    ]