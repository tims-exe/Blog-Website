from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    date = models.DateField()
    content = models.CharField(max_length=1000)