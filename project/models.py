from django.db import models

# Create your models here.
# class User(models.Model):
#     profile_pic=models.ImageField(null=True)
#     bio=models.TextField(max_length=100,null=False)
#     project=models.CharField(max_length=100,null=False)
#     contact=models.CharField(max_length=20,null=False)

#     def __str__(self):
#         return self.project

class PostProjects(models.Model):
    name=models.CharField(max_length=50,null=False)
    projects=models.FileField(max_length=100,null=False)
    
    def __str__(self):
        return self.name