# Generated by Django 3.0.3 on 2020-03-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0021_auto_20200304_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='description',
            field=models.TextField(default='There is no description added.', max_length=5000),
        ),
        migrations.AlterField(
            model_name='library',
            name='phone',
            field=models.CharField(default='No number provided.', max_length=100),
        ),
    ]
