# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lighthouseapp', '0006_auto_20151017_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='location',
        ),
        migrations.AddField(
            model_name='resource',
            name='city',
            field=models.CharField(null=True, max_length=150),
        ),
        migrations.AddField(
            model_name='resource',
            name='country',
            field=django_countries.fields.CountryField(default=datetime.datetime(2015, 10, 18, 9, 56, 9, 186664, tzinfo=utc), max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='group',
            field=models.CharField(max_length=2, choices=[('FE', 'Identified as female'), ('LG', 'LGBTQI'), ('RA', 'Race'), ('AL', 'All')]),
        ),
    ]
