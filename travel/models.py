# Create your models here.
from django.db import models

class Dest(models.Model):

    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    price=models.IntegerField
    offer=models.BooleanField(default=False)