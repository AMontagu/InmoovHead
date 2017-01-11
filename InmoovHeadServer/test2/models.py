from django.db import models

# Create your models here.

class Robot(models.Model):
    name = models.TextField()
    serialNumer = models.TextField()