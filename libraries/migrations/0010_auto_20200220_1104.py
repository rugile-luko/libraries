# Generated by Django 3.0.3 on 2020-02-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0009_auto_20200220_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
