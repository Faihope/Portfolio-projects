from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt



class PostProjects(models.Model):
    title = models.CharField(max_length=150)
    description = HTMLField()
    link= models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    screenshot1 = models.ImageField(upload_to='screenshots/')
    screenshot2 = models.ImageField(upload_to='screenshots/')
    screenshot3 = models.ImageField(upload_to='screenshots/')
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)

    
    def __str__(self):
        return self.title

class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/',default=0)
    description = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
   