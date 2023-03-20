from django.db import models
import uuid


# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True,blank=True)
    body = models.TextField(max_length=400,null=True)
    slug = models.SlugField(null=True)
    created = models.DateTimeField(auto_now_add=True)

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
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
