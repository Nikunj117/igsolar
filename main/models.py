from django.db import models
from django.contrib.auth.models import User
from .mail import SendWelcomMail
from django.utils.text import slugify

class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SolarSystem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    specifications = models.TextField()

class HeatPump(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    specifications = models.TextField()

class Appointment(TimeStampModel):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    services = models.CharField(max_length=100, null=True)
    comments = models.TextField(null=True)

class contactus(TimeStampModel):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=14)
    services = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=100, null=True)
    comments = models.TextField(null=True)


class contactusnew(TimeStampModel):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=14)
    existing_customer = models.CharField(max_length=100, null=True)
    enquiry_type = models.CharField(max_length=100, null=True)
    callback_team = models.TextField(null=True)

class UserMail(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email
    
    # def save(self, args, *kwargs):
    #     SendWelcomMail(self.email)
    #     super(UserMail, self).save(*args, **kwargs)

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# Add similar models for Aircons and Battery Storage
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title