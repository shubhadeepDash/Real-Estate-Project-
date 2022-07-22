from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# Create your models here... comment
class Property(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.TextField()
    longitude = models.DecimalField(max_digits=11, decimal_places=7,null=True,blank=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=7,null=True,blank=True)
    length = models.DecimalField(max_digits=20, decimal_places=5)
    breadth = models.DecimalField(max_digits=20, decimal_places=5)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    pincode = models.IntegerField(default = 000000)
    city = models.CharField(max_length=40,null=True,blank=True)
    state = models.CharField(max_length=40,null=True,blank=True)
    country = models.CharField(max_length=40,null=True,blank=True)
    image = models.ImageField(default = 'default.jpg',upload_to='property_pics')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

