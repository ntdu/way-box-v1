# Generated by Django 3.1.1 on 2021-03-07 08:53

import biker.models.models_vehicle
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=200, null=True)),
                ('path', models.FileField(upload_to=biker.models.models_vehicle.content_file_name, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf', 'zip', 'rar'])])),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.IntegerField(choices=[(100, 'Mới tạo'), (200, 'Chấp nhận'), (300, 'Từ chối')], default=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biker.route'),
        ),
        migrations.CreateModel(
            name='VerifyVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VerifyVehicle_created_by', to=settings.AUTH_USER_MODEL)),
                ('identity_card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='VerifyVehicle_identity_card', to='biker.media')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='VerifyVehicle_image', to='biker.media')),
                ('image_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='VerifyVehicle_image_vehicle', to='biker.media')),
                ('last_updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VerifyVehicle_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registration_certificate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='VerifyVehicle_registration_certificate', to='biker.media')),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='verify_vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biker.verifyvehicle'),
        ),
    ]