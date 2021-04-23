# Generated by Django 3.1.1 on 2021-04-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biker', '0012_auto_20210416_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biker',
            name='account',
        ),
        migrations.RemoveField(
            model_name='biker',
            name='address',
        ),
        migrations.RemoveField(
            model_name='biker',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='biker',
            name='email',
        ),
        migrations.RemoveField(
            model_name='biker',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='biker',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='biker',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='biker',
            name='password',
        ),
        migrations.RemoveField(
            model_name='biker',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='biker',
            name='plate_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='biker',
            name='ssn',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='biker',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='biker',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
