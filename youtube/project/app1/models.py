from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    creatname = models.CharField(max_length=50)
    subnum = models.CharField(max_length=10) 
    like = models.IntegerField()
    live= models.BooleanField()
    link1 = models.TextField()
    link2 = models.TextField()
    link3 = models.TextField()
