from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name
# Create your models here.