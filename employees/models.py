from django.db import models

# Create your models here.
class Employees(models.Model):
    name= models.CharField(max_length=100)
    age= models.FloatField()
    ci = models.IntegerField()
