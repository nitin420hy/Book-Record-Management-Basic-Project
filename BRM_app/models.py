from django.db import models

# Create your models here.
class Book(models.Model):
    Title=models.CharField(max_length=100)
    Price=models.FloatField()
    Author=models.CharField(max_length=100)
    Publisher=models.CharField(max_length=100)
