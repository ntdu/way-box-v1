# Generated by Django 3.1.1 on 2021-05-15 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_customerpoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('point_condition', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PointOfMoney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('point_accumulation', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.level')),
            ],
        ),
    ]
