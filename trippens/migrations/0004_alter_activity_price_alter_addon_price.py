# Generated by Django 4.1.5 on 2023-03-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trippens', '0003_activity_place_addon_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='addon',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
