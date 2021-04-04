from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone as tz
from .models_biker import *


class Path(models.Model):
    number = models.IntegerField() 
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Path_created_by")
    last_updated_date = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Path_last_updated_by")

    def __str__(self):
        return self.number


class Point(models.Model):
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=200)
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    sort = models.IntegerField()
    latitude  = models.DecimalField(decimal_places=2, max_digits=100)
    longtitude = models.DecimalField(decimal_places=2, max_digits=100)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Point_created_by")
    last_updated_date = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Point_last_updated_by")

    def __str__(self):
        return self.sort


class Route(models.Model):
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=200)
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Route_created_by")
    last_updated_date = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Route_last_updated_by")

    def __str__(self):
        return self.short_name