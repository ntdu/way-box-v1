from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone as tz
from customer.models import *
from .models_transport import *
from .models_product import *

class Shipment(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    pickup_point = models.ForeignKey(Point, on_delete=models.CASCADE)
    dropdown_point = models.ForeignKey(Point, on_delete=models.CASCADE)
    status_pickup = models.IntegerField() # chuyển thành enum
    status_process = models.IntegerField() # chuyển thành enum
    qr_code = models.CharField(max_length=200)
    datetime_pickup = models.DateTimeField(null=True, blank=True)
    datetime_plan = models.DateTimeField()
    ship_fee = models.DecimalField()
    total_value = models.DecimalField()
    discription = models.TextField(blank=True, null=True)
    capacity = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Transport_created_by")
    last_updated_date = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Transport_last_updated_by")

    def __str__(self):
        return self.transport + self.discription


class ShipmentLog(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)   
    description = models.TextField()

    def __str__(self):
        return self.discription


class ShipmentItem(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)   
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    description = models.TextField()
    amount = models.DecimalField()
    price = models.DecimalField()

    def __str__(self):
        return self.discription