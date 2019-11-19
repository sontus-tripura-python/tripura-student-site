from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='profile_pic', blank=True)
    university = models.CharField(max_length=100, blank=True)
    School = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=150, blank=True)
    fathername = models.CharField(max_length=50, blank=True)
    mothername = models.CharField(max_length=50, blank=True)
    deparment = models.CharField(max_length=50, blank=True)
    current_work = models.CharField(max_length=100, blank=True)
    religion = models.CharField(max_length=20, blank=True)
    Class = models.CharField(max_length=10, blank=True)
    Village = models.CharField(max_length=150, blank=True)
    thana = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=100, blank=True)
    current_city = models.CharField(max_length=100, blank=True)
    local_city = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    bio_data = models.TextField(blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class News(models.Model):
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
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    image = models.ImageField(upload_to='leaderpics', blank=True)

    def __str__(self):
        return self.name

class about(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    header = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    text = models.TextField()
    image = models.ImageField(upload_to='aboutpics', blank=True)

    def __str__(self):
        return self.header
class SubLeader(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='leaderpics', blank=True)

    def __str__(self):
        return self.name
