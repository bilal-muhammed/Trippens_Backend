# Generated by Django 4.1.5 on 2023-03-03 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trippens', '0001_initial'),
        ('user_managment', '0020_assignedcustomer_asigned_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='tour',
        ),
        migrations.AddField(
            model_name='customers',
            name='tours',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trippens.trippenstour'),
            preserve_default=False,
        ),
    ]