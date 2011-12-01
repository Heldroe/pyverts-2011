from django.db import models
from django.contrib.auth.models import User

class UserProfile (models.Model):
    user = models.ForeignKey(User, unique=True)
    test = models.CharField(max_length=30, blank=True, default="hello")
    test2 = models.IntegerField(blank=True, default=42)
