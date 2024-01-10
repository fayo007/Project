from django.db import models

from django.db import models

class Service(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.CharField(max_length = 255)

class AboutCompany(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    icon = models.CharField(max_length = 255)
    
class Work(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.CharField(max_length = 255)
    
    
class Team(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    icon = models.CharField(max_length = 255)
    

class DoWork(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.CharField(max_length = 255)
    
    
class OurStrength(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    photo = models.ImageField()
    
class Price(models.Model):
    text = models.TextField()
    title = models.CharField(max_length = 255)
    price = models.SmallIntegerField((""))()
    icon = models.CharField(max_length = 255)
    
class Project(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    photo = models.ImageField()
    

class Contact(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    phone = models.CharField(max_length = 14)
    subject = models.CharField(max_length = 255)
    message = models.TextField()
    icon = models.CharField(max_length = 255)






