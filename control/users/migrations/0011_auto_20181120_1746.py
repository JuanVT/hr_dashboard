# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-20 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_hruser_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeoffrequest',
            old_name='holiday_status',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='hruser',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=b'images'),
        ),
    ]
