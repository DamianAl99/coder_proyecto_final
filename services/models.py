from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=50)
    duration = models.CharField(max_length=15)
    description= models.CharField(max_length=150)