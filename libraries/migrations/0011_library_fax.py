# Generated by Django 3.0.3 on 2020-02-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0010_auto_20200220_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='fax',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
