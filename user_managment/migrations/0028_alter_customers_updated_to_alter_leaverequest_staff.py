# Generated by Django 4.1.5 on 2023-03-10 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_managment', '0027_alter_customers_updated_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='updated_to',
            field=models.DateField(null=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]