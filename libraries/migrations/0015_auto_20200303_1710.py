# Generated by Django 3.0.3 on 2020-03-03 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0014_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='longitude',
            new_name='longtitude',
        ),
    ]
