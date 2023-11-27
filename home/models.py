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
    pro_brand=models.CharField(max_length=50)
    pro_rating=models.FloatField()
    pro_image=models.ImageField( upload_to='uploads', height_field=None, width_field=None, max_length=None)
    is_available=models.BooleanField(default=True)