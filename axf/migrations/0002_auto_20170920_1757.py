# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='marketprice',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
    ]