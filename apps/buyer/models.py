from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Buyer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(
        User, related_name='buyer', on_delete=models.CASCADE)
    # products = models.

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    
