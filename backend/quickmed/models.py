from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    hospital_name = models.TextField(max_length=100)
    hospital_address = models.TextField(max_length=100)
    hospital_phone = models.TextField(max_length=100)

    def __str__(self):
        return self.user.username

class Result(models.Model):
    test_type = models.CharField(max_length=100)
    test_results = models.CharField(max_length=100)
    date = datetime.now()
    notes = models.TextField(max_length= 500)

    def __str__(self):
        return self.user.username

class Statistics(models.Model):
    tests_today = int
    tests_this_week = int
    tests_this_month = int
    test_all = int
