# Generated by Django 3.0.3 on 2020-03-03 10:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0011_library_fax'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]