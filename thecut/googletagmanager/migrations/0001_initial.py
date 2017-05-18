# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('container_id', models.CharField(max_length=25, verbose_name='Container ID')),
                ('is_enabled', models.BooleanField(default=False, help_text='Is the Google Tag Manager snippet enabled on the website?', verbose_name='enabled')),
                ('site', models.OneToOneField(related_name='+', on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'ordering': ['site'],
            },
        ),
    ]
