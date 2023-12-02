from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DeliveryAddress(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.IntegerField(unique=True)
    altmob=models.IntegerField(unique=True)
    pincode=models.IntegerField()
    address=models.TextField()
    dtype=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    def __str__(self) :
        return f"{self.username}"
class Products(models.Model):
    pro_name=models.CharField( max_length=50)
    pro_desc=models.CharField( max_length=50)
    pro_price=models.IntegerField()
    category=models.CharField(max_length=50)
    pro_brand=models.CharField(max_length=50)
    pro_rating=models.FloatField()
    pro_image=models.ImageField( upload_to='uploads', height_field=None, width_field=None, max_length=None)
    is_available=models.BooleanField(default=True)
class Cart(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    item_name=models.CharField( max_length=50)
    item_price=models.IntegerField()
class DeliverProducts(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    orderd_at=models.DateTimeField( auto_now_add=True)
    quantity=models.IntegerField()
    paymentmod=models.CharField( max_length=50,default="COD")
    total_amount=models.BooleanField()
    Status=models.CharField( max_length=50,default="pending")