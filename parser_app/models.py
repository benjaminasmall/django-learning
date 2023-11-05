from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Parser(models.Model):
    mpanCore = models.CharField(max_length=13)
    serialNo = models.CharField(max_length=10)
    unique_serial = models.IntegerField()
    ReadingDt = models.DateTimeField()
    readingVal = models.DecimalField(max_digits=10, decimal_places=1)

