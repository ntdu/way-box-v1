from django.db import models
from django.utils import timezone as tz
from customer.models import *

class Biker(models.Model):
    phone_number = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=12)
    plate_number = models.CharField(max_length=30)
    # capacity = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return '{0} - {1}'.format(self.phone_number, self.plate_number)


class BikerLog(models.Model):
    biker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="BikerLog_biker")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="BikerLog_customer")
    origin_lng = models.DecimalField(default=0, max_digits=9, decimal_places=6) 
    origin_lat = models.DecimalField(default=0, max_digits=9, decimal_places=6) 
    destination_lng = models.DecimalField(default=0, max_digits=9, decimal_places=6) 
    destination_lat = models.DecimalField(default=0, max_digits=9, decimal_places=6) 
    address_origin = models.TextField() 
    address_destination = models.TextField() 
    
    is_ride_confirmed = models.BooleanField(default=False)
    is_ride_cancelled = models.BooleanField(default=False)
    _id = models.CharField(max_length=255, null=True, blank=True)
    _v = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(default=0)
    ride_hash = models.TextField()
    date = models.DateTimeField(default=tz.now)

    created_date = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="BikerLog_created_by")

    def __str__(self):
        return '{0} - {1}'.format(self.biker, self.date.strftime('%d/%m/%Y'))