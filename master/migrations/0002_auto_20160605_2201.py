# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='image',
            field=models.ImageField(upload_to='testimonial_pics'),
        ),
    ]
