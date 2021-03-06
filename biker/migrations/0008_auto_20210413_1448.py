# Generated by Django 3.1.7 on 2021-04-13 07:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20210405_0217'),
        ('biker', '0007_auto_20210413_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikerLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_lng', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('origin_lat', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('destination_lng', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('destination_lat', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('address_origin', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('address_destination', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('isRideConfirmed', models.BooleanField(default=False)),
                ('isRideCancelled', models.BooleanField(default=False)),
                ('_id', models.CharField(max_length=20)),
                ('_v', models.CharField(max_length=20)),
                ('price', models.IntegerField(default=0)),
                ('rideHash', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('biker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BikerLog_biker', to='customer.user')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BikerLog_customer', to='customer.user')),
            ],
        ),
        migrations.DeleteModel(
            name='BikerHistory',
        ),
    ]
