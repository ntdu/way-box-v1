# Generated by Django 3.1.7 on 2021-03-29 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biker', '0005_auto_20210326_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biker',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='biker',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='biker',
            name='last_updated_by',
        ),
        migrations.RemoveField(
            model_name='biker',
            name='last_updated_date',
        ),
    ]
