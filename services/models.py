from django.db import models
from django.contrib.auth.models import User


class Specialservice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title
    
class Skills(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Team(models.Model):
    image = models.ImageField(upload_to='services' , default='default.jpg')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    instagram = models.CharField(max_length=220 , default='#')
    telegram = models.CharField(max_length=220 , default='#')
    # facebook = models.CharField(max_length=220 , default='#')
    # twitter = models.CharField(max_length=220 , default='#')
    # linkedin = models.CharField(max_length=220 , default='#')



    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.user.username

    def truncate_char(self):
        return str(self.description)[:10]

    
    
# Create your models here.
