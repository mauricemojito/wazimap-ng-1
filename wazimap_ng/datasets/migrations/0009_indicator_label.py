# Generated by Django 2.2.9 on 2019-12-20 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0008_auto_20191220_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='label',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]