# Generated by Django 3.0.3 on 2020-03-03 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0017_auto_20200303_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location_name',
            new_name='library',
        ),
    ]
