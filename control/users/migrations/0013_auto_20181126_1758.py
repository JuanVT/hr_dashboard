# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20181123_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hruser',
            name='profile_picture',
            field=models.ImageField(default=b'images/default.png', upload_to=b'images'),
        ),
    ]
