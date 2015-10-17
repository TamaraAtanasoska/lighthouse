# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='profile_images', blank=True)),
                ('location', models.CharField(max_length=150)),
                ('category', models.CharField(choices=[('ME', 'Meetup'), ('CO', 'Conference'), ('UN', 'Universities'), ('MS', 'Mentorship'), ('JP', 'Job portal'), ('LG', 'Learners groups'), ('NT', 'Networks'), ('HA', 'Hackaton'), ('OT', 'Other')], max_length=2)),
                ('aspiration', models.CharField(choices=[('ME', 'Meetup'), ('CO', 'Conference'), ('UN', 'Universities'), ('MS', 'Mentorship'), ('JP', 'Job portal'), ('LG', 'Learners groups'), ('NT', 'Networks'), ('HA', 'Hackaton'), ('OT', 'Other')], max_length=2)),
                ('group', models.CharField(choices=[('ME', 'Meetup'), ('CO', 'Conference'), ('UN', 'Universities'), ('MS', 'Mentorship'), ('JP', 'Job portal'), ('LG', 'Learners groups'), ('NT', 'Networks'), ('HA', 'Hackaton'), ('OT', 'Other')], max_length=2)),
                ('level', models.CharField(choices=[('ME', 'Meetup'), ('CO', 'Conference'), ('UN', 'Universities'), ('MS', 'Mentorship'), ('JP', 'Job portal'), ('LG', 'Learners groups'), ('NT', 'Networks'), ('HA', 'Hackaton'), ('OT', 'Other')], max_length=2)),
            ],
        ),
    ]
