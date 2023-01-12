from django.db import models

class Schedules(models.Model):
    cliente = models.CharField(max_length=50)
    services = models.CharField(max_length=50)