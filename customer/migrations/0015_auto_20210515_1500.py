# Generated by Django 3.1.1 on 2021-05-15 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_level_pointofmoney'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pointofmoney',
            old_name='money',
            new_name='money_condition',
        ),
    ]
