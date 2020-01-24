from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE = ( 
        ('manager', 'Manager'), 
        ('employee', 'Employee'), 
    ) 
    age = models.PositiveIntegerField(null=True, blank=True)
    role = models.CharField(max_length=10,  
                              choices=USER_TYPE, 
                              ) 