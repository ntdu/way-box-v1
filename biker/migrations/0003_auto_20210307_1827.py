# Generated by Django 3.1.7 on 2021-03-07 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biker', '0002_auto_20210307_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='status',
            new_name='verify_status',
        ),
    ]
