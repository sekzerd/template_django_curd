from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=18)
    age = models.IntegerField()
    address = models.CharField(max_length=32)
