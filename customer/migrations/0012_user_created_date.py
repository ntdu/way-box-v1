# Generated by Django 3.1.1 on 2021-04-23 06:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20210423_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
