# Generated by Django 3.1.1 on 2021-04-23 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_remove_user_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='encoded_password',
            new_name='password',
        ),
    ]
