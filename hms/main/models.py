from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    u_joined_at = models.DateTimeField(auto_now_add=True)
    u_phone = models.CharField(max_length=11, null=True, blank=True)
    u_email = models.CharField(max_length=30, null=True, blank=True)
    u_isAdmin = models.BooleanField(default=False)


class Excercise(models.Model):
    e_category = models.CharField(max_length=20)
    e_name = models.CharField(max_length=20)
    e_description = models.TextField(max_length=20)
    e_recommend_count = models.IntegerField(default=0)
    e_created_at = models.DateTimeField(auto_now_add=True)
    e_modified_at = models.DateTimeField(auto_now=True)
