# Generated by Django 3.1.1 on 2021-04-23 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_user_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_date',
        ),
    ]
