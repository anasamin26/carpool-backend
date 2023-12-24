# Generated by Django 5.0 on 2023-12-19 12:38

import django.contrib.postgres.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('avatar', models.CharField(default='https://bootdey.com/img/Content/avatar/avatar1.png', max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=1)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('organizer_id', models.CharField(max_length=255)),
                ('organizer', models.CharField(max_length=255)),
                ('organizer_occupation', models.CharField(max_length=255)),
                ('organizer_image', models.CharField(default='https://bootdey.com/img/Content/avatar/avatar1.png', max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('status', models.CharField(max_length=1)),
                ('from_location', models.CharField(max_length=255)),
                ('to_location', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField()),
                ('total_fare', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car', models.CharField(max_length=255)),
                ('background_colors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None)),
                ('title_color', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=255)),
                ('attendees', models.ManyToManyField(related_name='rides_attending', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
