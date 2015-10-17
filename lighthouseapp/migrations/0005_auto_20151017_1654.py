# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lighthouseapp', '0004_auto_20151017_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='level',
            field=models.CharField(max_length=2, choices=[('BG', 'Beginner'), ('IN', 'Intermediate'), ('AD', 'Advanced'), ('AL', 'All')]),
        ),
    ]
