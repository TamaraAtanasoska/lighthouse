# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lighthouseapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='link',
            field=models.CharField(default=datetime.datetime(2015, 10, 17, 13, 28, 50, 836256, tzinfo=utc), max_length=150),
            preserve_default=False,
        ),
    ]
