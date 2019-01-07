# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-03 18:06
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='HRUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('bio', models.TextField(blank=True, max_length=700)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('remaining_holiday', models.DecimalField(decimal_places=1, default=25.0, max_digits=3)),
                ('job_title', models.CharField(blank=True, max_length=30)),
                ('start_date', models.DateField()),
                ('nationality', models.CharField(blank=True, max_length=30)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('post_code', models.CharField(blank=True, max_length=30)),
                ('employee_id', models.CharField(blank=True, max_length=30)),
                ('gender', models.CharField(blank=True, choices=[(b'male', b'Male'), (b'female', b'Female')], max_length=10, null=True)),
                ('private_phone', models.DecimalField(blank=True, decimal_places=0, max_digits=30, null=True)),
                ('work_phone', models.DecimalField(blank=True, decimal_places=0, max_digits=30, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=30)),
                ('account_number', models.DecimalField(blank=True, decimal_places=0, max_digits=30, null=True)),
                ('bank_account_type', models.CharField(blank=True, max_length=30)),
                ('swift_code', models.CharField(blank=True, max_length=30)),
                ('iban', models.CharField(blank=True, max_length=30)),
                ('nin', models.CharField(blank=True, max_length=30)),
                ('tax_code', models.CharField(blank=True, max_length=30)),
                ('emergency_first_name', models.CharField(blank=True, max_length=30)),
                ('emergency_last_name', models.CharField(blank=True, max_length=30)),
                ('emergency_contact_number', models.DecimalField(blank=True, decimal_places=0, max_digits=30, null=True)),
                ('status', models.CharField(blank=True, choices=[(b'active', b'Active'), (b'inactive', b'Inactive')], max_length=10, null=True)),
                ('profile_picture', models.ImageField(default=b'images/default.png', upload_to=b'images')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TimeOffRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_request', models.DateField(blank=True)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('description', models.TextField(blank=True, max_length=600)),
                ('status', models.CharField(choices=[(b'approved', b'Approved'), (b'pending_approval', b'Pending Approval'), (b'not_approved', b'Not Approved')], default=b'pending_approval', max_length=30)),
                ('type', models.CharField(choices=[(b'holiday', b'Holiday'), (b'off_sick', b'Off Sick'), (b'working_from_home', b'Working From Home')], default=b'holiday', max_length=20)),
                ('all_day', models.CharField(choices=[(b'all_day', b'All Day'), (b'morning', b'Morning'), (b'afternoon', b'Afternoon')], default=b'all_day', max_length=10)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hruser',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Department'),
        ),
        migrations.AddField(
            model_name='hruser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='hruser',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hruser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
