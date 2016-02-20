from django.db import models
from django.contrib.auth.models import User
from enum import Enum


# Create your models here.

Design_Status = Enum('IN_PROGRESS', 'AVAILABLE')


class Administrator(models.Model):
    company = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    user = models.OneToOneField(User,null=True)

class Proyecto(models.Model):
    name = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=250,blank=True)
    estimated_price = models.BigIntegerField

class Designer(models.Model):
    name = models.CharField(max_length=50,blank=True)
    lastname = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)

class Design(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    status = Design_Status
    price = models.BigIntegerField
    imageFile = models.ImageField(upload_to='images',null=True)
    designer = models.ForeignKey(Designer,null=True)

