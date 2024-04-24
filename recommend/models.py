from django.db import models

# Create your models here.

from .data import specialists


specialist_choices = [(i,i) for i in specialists]


class Doctor(models.Model):
    name = models.CharField(max_length=500)
    specialisation = models.CharField(max_length=500, choices=specialist_choices)

