# Generated by Django 4.1.5 on 2023-02-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_managment', '0006_remove_customers_staffbranch_customers_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='tour',
            field=models.CharField(max_length=50, null=True),
        ),
    ]