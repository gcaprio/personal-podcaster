# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pocket_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PocketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pocket_id', models.IntegerField()),
                ('given_title', models.TextField()),
                ('given_url', models.URLField()),
                ('resolved_id', models.IntegerField()),
                ('resolved_title', models.TextField()),
                ('resolved_url', models.URLField()),
                ('downloaded_file', models.FileField(blank=None, null=True, upload_to='pocket_items')),
            ],
        ),
    ]
