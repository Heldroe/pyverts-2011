from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InterestCategory(models.Model):
    name = models.CharField(max_length=512)


class Interest(models.Model):
    name = models.CharField(max_length=512)
    fb_id = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(InterestCategory)


class UserInterests(models.Model):
    user = models.ForeignKey(User)
    interest = models.ForeignKey(Interest)
    created = models.DateField()
    
