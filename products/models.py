from django.db import models
from django.utils import timezone

# Create your models here.


class featuredproducts(models.Model):
    image=models.FileField(upload_to='images/')
    price=models.IntegerField(default=0)
    name=models.CharField(max_length=50,default='0')
    type=models.CharField(max_length=20)
    summary=models.TextField(default='0')
    time=models.DateTimeField(auto_now_add=timezone.now)


class ringsdatabase(models.Model):
    image=models.FileField(upload_to='images/')
    price=models.IntegerField(default=0)
    name=models.CharField(max_length=50,default='0')
    type=models.CharField(max_length=20,default='ring')
    summary=models.TextField(default='0')
    time=models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return self.name

class necklessdatabase(models.Model):
    image=models.FileField(upload_to='images/')
    price=models.IntegerField(default=0)
    name=models.CharField(max_length=50,default='0')
    type=models.CharField(max_length=20,default='necklace')
    summary=models.TextField(default='0')
    time=models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return self.name

class braceletsdatabase(models.Model):
    image=models.FileField(upload_to='images/')
    price=models.IntegerField(default=0)
    name=models.CharField(max_length=50,default='0')
    type=models.CharField(max_length=20,default='bracelet')
    summary=models.TextField(default='0')
    time=models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return self.name

class jewellarydatabase(models.Model):
    image=models.FileField(upload_to='images/')
    price=models.IntegerField(default=0)
    name=models.CharField(max_length=50,default='0')
    type=models.CharField(max_length=20,default='jewellery')
    summary=models.TextField(default='0')
    time=models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return self.name

class earingsdatabase(models.Model):
    image=models.FileField(upload_to='images/')
    price=models.IntegerField(default=0)
    name=models.CharField(max_length=50,default='0')
    type=models.CharField(max_length=20,default='earing')
    summary=models.TextField(default='0')
    time=models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return self.name

class message(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    message=models.TextField()

class reviewdatabase(models.Model):
    name=models.CharField(max_length=50)
    review=models.TextField()
    star=models.IntegerField()
    code=models.IntegerField()
    time=models.DateTimeField(auto_now_add=timezone.now)

