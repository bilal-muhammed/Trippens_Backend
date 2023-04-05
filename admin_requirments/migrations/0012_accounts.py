# Generated by Django 4.1.5 on 2023-03-31 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_managment', '0037_audio'),
        ('admin_requirments', '0011_alter_tourform_child_count_custominetenary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('gst', models.IntegerField(default=5)),
                ('offer', models.IntegerField(default=0)),
                ('extra_amount', models.IntegerField(default=0)),
                ('is_done', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_managment.customers')),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_requirments.tourform')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]