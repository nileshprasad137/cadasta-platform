# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-08 10:12
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import jsonattrs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20160720_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpatialResource',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryCollectionField(blank=True, null=True, srid=4326)),
                ('attributes', jsonattrs.fields.JSONAttributeField(default=jsonattrs.fields.JSONAttributes)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spatial_resources', to='resources.Resource')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
