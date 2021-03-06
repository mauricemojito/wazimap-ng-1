# Generated by Django 2.2.8 on 2020-01-20 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0021_auto_20200110_0628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataset',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='datasetdata',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='geography',
            options={'ordering': ['id'], 'verbose_name_plural': 'geographies'},
        ),
        migrations.AlterModelOptions(
            name='indicator',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='indicatorcategory',
            options={'ordering': ['id'], 'verbose_name_plural': 'Indicator Categories'},
        ),
        migrations.AlterModelOptions(
            name='indicatorsubcategory',
            options={'ordering': ['id'], 'verbose_name_plural': 'Indicator Subcategories'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='profiledata',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='profileindicator',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='universe',
            options={'ordering': ['id']},
        ),
    ]
