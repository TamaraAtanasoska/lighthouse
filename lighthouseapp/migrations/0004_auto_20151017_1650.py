# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lighthouseapp', '0003_auto_20151017_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='aspiration',
            field=models.CharField(max_length=2, choices=[('PM', 'Product manager'), ('PR', 'Programming'), ('DE', 'Design'), ('AL', 'All')]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='category',
            field=models.CharField(max_length=2, choices=[('ME', 'Meetup'), ('CO', 'Conference'), ('UN', 'Universities'), ('MS', 'Mentorship'), ('JP', 'Job portal'), ('LG', 'Learners groups'), ('NT', 'Networks'), ('HA', 'Hackaton'), ('OT', 'Other'), ('AL', 'All')]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='group',
            field=models.CharField(max_length=2, choices=[('ST', 'Student'), ('UN', 'Unemployed'), ('OT', 'Other'), ('AL', 'All')]),
        ),
    ]
