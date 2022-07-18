from django.db import models
from django.contrib.auth.models import User

# Create your models here... comment
class Property(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.TextField()
    longitude = models.DecimalField(max_digits=11, decimal_places=7)
    latitude = models.DecimalField(max_digits=11, decimal_places=7)
    length = models.DecimalField(max_digits=20, decimal_places=5)
    breadth = models.DecimalField(max_digits=20, decimal_places=5)
    purpose = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PropertyPictures(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg",upload_to='property_pics')
