from django.db import models

# Create your models here.
class data(models.Model):
    symbol=models.CharField(max_length=100)
    data1=models.CharField(max_length=100)