from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    hospital_name = models.CharField(max_length=50)
    hospital_address = models.CharField(max_length=100)
    hospital_phone = models.CharField(max_length=50)
    card_number = models.CharField(max_length=20)
class Result(models.Model):
    test_type = models.CharField(max_length=300)
    test_results = models.CharField(max_length=300)
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    date = int
