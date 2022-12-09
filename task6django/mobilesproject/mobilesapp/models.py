from django.db import models

# Create your models here.
class Mobile (models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    make=models.CharField(max_length=100)
    desc=models.TextField()