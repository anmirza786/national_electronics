from email.headerregistry import Address
from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Buyer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=255,blank=True,null=True,verbose_name='Phone number')
    Address = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    created_by = models.OneToOneField(
        User, related_name='buyer', on_delete=models.CASCADE)
    # products = models.

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    
