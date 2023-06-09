# Generated by Django 4.1.5 on 2023-04-05 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trippens', '0005_alter_activity_price_alter_addon_price'),
        ('user_managment', '0037_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedItenearies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='fixed_itineary/')),
                ('date', models.DateField(auto_now_add=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trippens.trippenstour')),
            ],
        ),
    ]
