from django.db import models

# Create your models here.

def class InterestCategory()
    name = models.CharField(max_length=512)


def class Interest(models.Model):
    name = models.CharField(max_length=512)
    fb_id = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(InterestCategory)


def class UserInterests
    user = models.ForeignKey(User)
    interest = models.ForeignKey(Interest)
    created = models.DateField()
    
