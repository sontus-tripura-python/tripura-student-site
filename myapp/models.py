from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='profile_pic', blank=True)
    birthdate = models.DateField(null=True, blank=True)
    university = models.CharField(max_length=100, blank=True)
    School = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=150, blank=True)
    fathername = models.CharField(max_length=50, blank=True)
    mothername = models.CharField(max_length=50, blank=True)
    deparment = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField()
    current_work = models.CharField(max_length=100, blank=True)
    religion = models.CharField(max_length=20, blank=True)
    Class = models.CharField(max_length=10, blank=True)
    Village = models.CharField(max_length=150, blank=True)
    thana = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=100, blank=True)
    current_city = models.CharField(max_length=100, blank=True)
    local_city = models.CharField(max_length=100, blank=True)
    bio_data = models.TextField(blank=True)


    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='Newspic', blank=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class leadership(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='leaderpics', blank=True)

    def __str__(self):
        return self.name
