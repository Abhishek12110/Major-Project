from datetime import datetime
from email.headerregistry import Address
from statistics import mode
from turtle import title
from django.db import models
from django.contrib.auth.models import User,auth
# from ckeditor.fields import RichTextField
# from froala_editor.fields import FroalaField

# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=200)
    subcategory=models.CharField(max_length=200,blank=True)
    product_name= models.CharField(max_length=200)
    price = models.FloatField()
    discount_price=models.FloatField()
    image= models.ImageField(upload_to='shop/static/shop/images',blank=True)

class Blog(models.Model):
    title=models.CharField(default='',max_length=200)
    subtitle=models.CharField(default='',max_length=200,blank=True)
    image= models.ImageField(upload_to='shop/static/shop/images',blank=True)
    content = models.TextField()
    # content = FroalaField()
    timestamp=models.DateTimeField(null=True,blank=True)
    author = models.TextField(default='',blank=True)

class About(models.Model):
    heading=models.CharField(default='',max_length=200)
    subheading=models.CharField(default='',max_length=200,blank=True)
    content = models.TextField()
    author = models.TextField(default='',blank=True)
    footnote=models.CharField(default='',max_length=200)

class orderitem(models.Model):
    customer =models.CharField(max_length=50)
    product =models.CharField(max_length=2000)
    price=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    date=models.DateField(default=datetime.now)

    def placeorder(self):
        self.save()

