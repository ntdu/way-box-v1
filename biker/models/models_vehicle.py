from unidecode import unidecode
from django.db import models
from datetime import datetime
from enum import Enum
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils import timezone as tz
from django.conf import settings
from .models_biker import *
from .models_route import *


def content_file_name(instance, filename):
    new_name = unidecode.unidecode(filename)
    return 'vehicle_{0}/{1}/{2}'.format(instance.id, tz.now().strftime('%Y/%m/%d'), new_name)


class Media(models.Model):
    filename = models.CharField(null=True, blank=True, max_length=200)
    path = models.FileField(upload_to=content_file_name, 
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf', 'zip', 'rar'])])
    created_date = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return '{0}'.format(self.path)
        
    def display_file(self):
        return settings.MEDIA_URL + str(self.path)


class VerifyVehicleStatus(Enum):
    New = 100
    Accept = 200
    Reject = 300

    @classmethod
    def display(cls, value):
        if value == VerifyVehicleStatus.New.value:
            return 'Mới tạo'
        elif value == VerifyVehicleStatus.Accept.value:
            return 'Chấp nhận'
        elif value == VerifyVehicleStatus.Reject.value:
            return 'Từ chối'
        else:
            return ''

    @classmethod
    def choices(cls):
        return tuple((i.value, VerifyVehicleStatus.display(i.value)) for i in cls)

    @classmethod
    def parse(cls, value):
        if value.lower() == 'mới tạo': return VerifyVehicleStatus.New.value
        if value.lower() == 'chấp nhận': return VerifyVehicleStatus.Accept.value
        if value.lower() == 'từ chối': return VerifyVehicleStatus.Reject.value
        return None


class VerifyVehicle(models.Model):
    image = models.ForeignKey(Media, on_delete=models.PROTECT, related_name='VerifyVehicle_image')
    image_vehicle = models.ForeignKey(Media, on_delete=models.PROTECT, related_name='VerifyVehicle_image_vehicle')
    identity_card = models.ForeignKey(Media, on_delete=models.PROTECT, related_name='VerifyVehicle_identity_card')
    registration_certificate = models.ForeignKey(Media, on_delete=models.PROTECT, related_name='VerifyVehicle_registration_certificate')
    created_date = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="VerifyVehicle_created_by")
    last_updated_date = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="VerifyVehicle_last_updated_by")

    def __str__(self):
        return self.plate_number


class Vehicle(models.Model):
    biker = models.ForeignKey(Biker, on_delete=models.CASCADE) 
    verify_status = models.IntegerField(default=100, choices=VerifyVehicleStatus.choices())
    verify_vehicle = models.OneToOneField(VerifyVehicle, null=True, blank=True, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, null=True, blank=True, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=50)
    capacity = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Vehicle_created_by")
    last_updated_date = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Vehicle_last_updated_by")

    def __str__(self):
        return self.plate_number