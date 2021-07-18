from django.db import models

#Create your models here.
class User(models.Model):
    profile_pic=models.ImageField(null=True)
    bio=models.TextField(max_length=100,null=False)
    project=models.CharField(max_length=100,null=False)
    contact=models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.project

class PostProjects(models.Model):
    name=models.CharField(max_length=50,null=False)
    projects=models.FileField(max_length=100,null=False)
    
    def __str__(self):
        return self.name
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
