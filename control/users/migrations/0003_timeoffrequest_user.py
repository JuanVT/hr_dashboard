# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-09 21:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_timeoffrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeoffrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
