from django.db import models

# Create your models here.
class ImageData(models.Model):
    name = models.CharField(max_length=10,default=False)
    image = models.ImageField(upload_to="situation_image",default=False)