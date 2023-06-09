from django.contrib.auth.models import User
from django.db import models
import uuid
from ckeditor.fields import RichTextField
# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True,blank=True)
    body = RichTextField(null=True)
    slug = models.SlugField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    github_link = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title

    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ""
        return url


class Skills(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(default="skkillogo.png",null=True, blank=True)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def imageURL(self):
        try:
            url = self.logo.url
        except:
            url = ""
        return url


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Messages(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True,blank=True)
    subject = models.CharField(max_length=200,null=True)
    body = models.TextField(null=True)
    is_read = models.BooleanField(default=False,)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    # user = models.ForeignKey(User,on_delete=models.SET_NULL)
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name