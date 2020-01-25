# Generated by Django 2.2.8 on 2020-01-24 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0022_auto_20200120_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileHighlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Name of the indicator in the database', max_length=60)),
                ('label', models.CharField(blank=True, help_text='Label for the indicator displayed on the front-end', max_length=60)),
                ('indicator', models.ForeignKey(help_text='Indicator on which this highlight is based on.', on_delete=django.db.models.deletion.CASCADE, to='datasets.Indicator')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Profile')),
                ('universe', models.ForeignKey(blank=True, help_text='The subset of the population considered for this indicator.', null=True, on_delete=django.db.models.deletion.CASCADE, to='datasets.Universe')),
            ],
        ),
    ]