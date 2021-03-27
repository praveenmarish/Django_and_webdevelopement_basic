from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=20)
    pin=models.CharField(max_length=6)

class MultipleImageUpload(models.Model):
    images = models.ImageField()
    