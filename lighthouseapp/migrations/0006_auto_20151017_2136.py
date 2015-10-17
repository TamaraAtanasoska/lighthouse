# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lighthouseapp', '0005_auto_20151017_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='status',
            field=models.CharField(max_length=2, default=datetime.datetime(2015, 10, 17, 19, 36, 53, 11204, tzinfo=utc), choices=[('ST', 'Student'), ('UN', 'Unemployed'), ('OT', 'Other'), ('AL', 'All')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='aspiration',
            field=models.CharField(max_length=2, choices=[('PM', 'Product manager'), ('PR', 'Programming'), ('DE', 'Product Design'), ('AL', 'All')]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='group',
            field=models.CharField(max_length=2, choices=[('FE', 'Identified as female'), ('LG', 'LGBTQI'), ('RA', 'Race')]),
        ),
    ]
