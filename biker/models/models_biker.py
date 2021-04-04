from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone as tz

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