from django.db import models
from django.utils import timezone as tz

class User(models.Model):
    phone_number = models.CharField(max_length=15, primary_key=True)
    email = models.TextField(null=True, blank=True, unique=True)
    password = models.TextField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    female = models.BooleanField()                                 
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=225, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return self.first_name


class CustomerPoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    point = models.DecimalField(default=0, max_digits=9, decimal_places=2)                            
    expired_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=tz.now)
    
    def __str__(self):
        return '{0} - {1}'.format(self.user.first_name, self.point)


class Level(models.Model):
    code = models.CharField(null=True, blank=True, max_length=50)
    name = models.CharField(null=True, blank=True, max_length=50)
    point_condition = models.IntegerField()
    point_accumulation = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.point_condition)