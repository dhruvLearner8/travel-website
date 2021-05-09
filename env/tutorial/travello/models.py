from django.db import models

# Create your models here.
class destination(models.Model):
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField(default=0)
    offer= models.BooleanField(default=False)