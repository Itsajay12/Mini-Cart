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
    