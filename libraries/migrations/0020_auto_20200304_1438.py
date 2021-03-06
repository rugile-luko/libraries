# Generated by Django 3.0.3 on 2020-03-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0019_auto_20200303_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='library',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9, null=True),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
