from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    university = models.CharField(max_length=100, blank=True)
    School = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=150, blank=True)
    fathername = models.CharField(max_length=50)
    mothername = models.CharField(max_length=50)
    deparment = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True)
    Village = models.CharField(max_length=150)
    thana = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    current_city = models.CharField(max_length=100)
    local_city = models.CharField(max_length=100)
    bio_data = models.TextField(blank=True)


def __str__(self):
    return 'Profile of user{}.format(self.user.username)'
