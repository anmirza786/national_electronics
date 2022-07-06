from io import BytesIO
from tkinter import HIDDEN
from PIL import Image

from django.core.files import File
from django.db import models

# from apps.vendor.models import Vendor


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title
    def save(self):
        slug=self.title
        slug = slug.lower()
        slug = slug.replace(" ","_")
        self.slug = slug
        return super().save()
class ProductStatusEnum(models.IntegerChoices):
    SOON = 1 ,'Comming Soon'
    AVAILABLE = 2 , 'Available'
    OUTOFSTOCK = 3 , 'Out of Stock'

class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    # vendor = models.ForeignKey(
    #     Vendor, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    available_quantity = models.IntegerField(blank=False,null=False,verbose_name='Quantity Available',help_text='Enter the Available Quantity Greater than 0',default=0)
    product_status = models.SmallIntegerField(choices=ProductStatusEnum.choices,default=ProductStatusEnum.AVAILABLE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.FileField(blank=True)
    # thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title
    def save(self):
        slug=self.title
        slug = slug.lower()
        slug = slug.replace(" ","_")
        self.slug = slug
        return super().save()
    
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/',
                              null=False,
                              blank=False)
    # thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    def __str__(self):
        return f'image:({str(id)})'
