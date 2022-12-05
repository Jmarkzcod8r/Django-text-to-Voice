from django.db import models

# Create your models here.
class Section(models.Model):
  name = models.CharField(max_length=255, blank=False, null=True,)

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=255, blank=False, null=True,)
  section = models.ForeignKey(Section,on_delete=models.CASCADE)

class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()

class Testimony (models.Model):
    title=models.TextField( unique=True)