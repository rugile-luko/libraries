# Generated by Django 3.0.3 on 2020-02-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0003_auto_20200217_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='review',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
