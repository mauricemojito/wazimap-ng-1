# Generated by Django 2.2.10 on 2020-03-30 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20200319_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoroplethMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
