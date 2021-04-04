from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone as tz
from customer.models import *
from .models_vehicle import *


class Transport(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    status = models.IntegerField()                                # chuyển thành dạng enum
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Transport_created_by")
    last_updated_date = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Transport_last_updated_by")

    def __str__(self):
        return self.vehicle + self.product_category


class Rating(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE) 
    description = models.TextField()
    star  = models.IntegerField()

    def __str__(self):
        return self.description 


class TransportLog(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE) 
    description = models.TextField()

    def __str__(self):
        return self.description 