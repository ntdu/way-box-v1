# Generated by Django 3.1.7 on 2021-04-02 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210402_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_updated_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_updated_date',
        ),
    ]