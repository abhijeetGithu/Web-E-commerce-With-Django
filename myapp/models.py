from django.db import models

# Create your models here.
class Feature(models.Model):
    name= models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    image = models.ImageField(upload_to='feature_images/', default='feature_images/car.jpeg') 
