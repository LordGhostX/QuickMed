from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class Result(models.Model):
    test_type = models.CharField(max_length=300)
    test_results = models.CharField(max_length=300)
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    date = int

class Hospital(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)
