# Generated by Django 4.1.5 on 2023-03-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trippens', '0004_alter_activity_price_alter_addon_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='price',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='addon',
            name='price',
            field=models.FloatField(default=0, null=True),
        ),
    ]