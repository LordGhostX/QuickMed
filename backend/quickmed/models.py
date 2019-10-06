from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    hospital_address = models.CharField(max_length=100)
    hospital_phone = models.CharField(max_length=100)

class Result(models.Model):
    test_type = models.CharField(max_length=100)
    test_results = models.CharField(max_length=100)
    date = datetime.now()
