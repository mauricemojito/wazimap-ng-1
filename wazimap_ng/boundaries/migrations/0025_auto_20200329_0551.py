# Generated by Django 2.2.10 on 2020-03-29 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boundaries', '0024_auto_20200329_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geographyboundary',
            name='geography',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='datasets.Geography'),
        ),
    ]
