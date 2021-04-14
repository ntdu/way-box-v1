from django.db import models
from django.utils import timezone as tz
from customer.models import *

class Biker(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    gender = models.BooleanField()                                  # False: girl 
    phone_number = models.CharField(max_length=12)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=225, null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    # created_date = models.DateTimeField(default=tz.now)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Biker_created_by")
    # last_updated_date = models.DateTimeField(null=True, blank=True)
    # last_updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="Biker_last_updated_by")
    
    def __str__(self):
        return self.first_name + self.last_name


class BikerLog(models.Model):
    biker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="BikerLog_biker")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="BikerLog_customer")
    origin_lng = models.DecimalField(default=0, max_digits=9, decimal_places=6) 
    origin_lat = models.DecimalField(default=0, max_digits=9, decimal_places=6) 
    destination_lng = models.DecimalField(default=0, max_digits=9, decimal_places=6) 
    destination_lat = models.DecimalField(default=0, max_digits=9, decimal_places=6) 
    address_origin = models.TextField() 
    address_destination = models.TextField() 
    
    isRideConfirmed = models.BooleanField(default=False)
    isRideCancelled = models.BooleanField(default=False)
    _id = models.CharField(max_length=255, null=True, blank=True)
    _v = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(default=0)
    rideHash = models.TextField()
    date = models.DateTimeField(default=tz.now)

    created_date = models.DateTimeField(default=tz.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="BikerLog_created_by")

    def __str__(self):
        return '{0} - {1}'.format(self.biker, self.date.strftime('%d/%m/%Y'))