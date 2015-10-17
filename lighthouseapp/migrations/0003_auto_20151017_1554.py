# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lighthouseapp', '0002_resource_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='aspiration',
            field=models.CharField(max_length=2, choices=[('PM', 'Product manager'), ('PR', 'Programming'), ('DE', 'Design')]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='group',
            field=models.CharField(max_length=2, choices=[('ST', 'Student'), ('UN', 'Unemployed'), ('OT', 'Other')]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='level',
            field=models.CharField(max_length=2, choices=[('BG', 'Beginner'), ('IN', 'Intermediate'), ('AD', 'Advanced')]),
        ),
    ]
