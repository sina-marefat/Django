from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Education(models.Model):
    university = models.CharField(max_length=100)
    term = models.IntegerField()
    enterYear = models.IntegerField()
    payOrFree = models.BooleanField()
    date = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)


