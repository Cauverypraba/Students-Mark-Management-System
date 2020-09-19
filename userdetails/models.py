from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    mark1 = models.IntegerField(blank=True, default=0)
    mark2 = models.IntegerField(blank=True, default=0)
    mark3 = models.IntegerField(blank=True, default=0)