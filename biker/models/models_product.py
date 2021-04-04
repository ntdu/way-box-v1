from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone as tz
from .models_vehicle import *


class ProductCategory(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.code


class VehicleProductCategory(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE) 
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="VehicleProductCategory_created_by")
    last_updated_date = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="VehicleProductCategory_last_updated_by")

    def __str__(self):
        return self.vehicle + self.product_category


class Product(models.Model): 
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Product_created_by")
    last_updated_date = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Product_last_updated_by")

    def __str__(self):
        return self.name