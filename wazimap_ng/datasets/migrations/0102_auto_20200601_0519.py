# Generated by Django 2.2.10 on 2020-06-01 05:19

import django.core.validators
from django.db import migrations, models
import wazimap_ng.datasets.models.upload


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0101_auto_20200531_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetfile',
            name='dataset_id',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
