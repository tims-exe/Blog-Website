from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    content = models.CharField(max_length=1000)