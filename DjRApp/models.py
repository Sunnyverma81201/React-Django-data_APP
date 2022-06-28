from django.db import models

# Create your models here.

class ObjectDetectionData(models.Model):
    images_name = models.CharField(primary_key=True,max_length=200)
    objects_detected = models.CharField(max_length=600)
    timestamp = models.DateField()