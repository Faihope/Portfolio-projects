from django.db import models

# Create your models here.
class User(models.Model):
    profile_pic=models.ImageField(null=True)
    bio=models.TextField(max_length=100,null=False)
    project=models.CharField(max_length=100,null=False)
    contact=models.CharField(max_length=20,null=False)