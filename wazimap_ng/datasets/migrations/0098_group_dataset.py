# Generated by Django 2.2.10 on 2020-05-31 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0097_auto_20200531_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='dataset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasets.Dataset'),
        ),
    ]