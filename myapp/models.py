from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='profile_pic')
    birthdate = models.DateField(null=True, blank=True)
    university = models.CharField(max_length=100, blank=True)
    School = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=150, blank=True)
    fathername = models.CharField(max_length=50, blank=True)
    mothername = models.CharField(max_length=50, blank=True)
    deparment = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField()
    Village = models.CharField(max_length=150, blank=True)
    thana = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=100, blank=True)
    current_city = models.CharField(max_length=100, blank=True)
    local_city = models.CharField(max_length=100, blank=True)
    bio_data = models.TextField(blank=True)


    def __str__(self):
        return self.user.username
