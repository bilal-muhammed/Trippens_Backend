# Generated by Django 4.1.5 on 2023-02-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_managment', '0018_assignedcustomer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='is_asigned',
            field=models.BooleanField(default=False),
        ),
    ]
