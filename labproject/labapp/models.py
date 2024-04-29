
from django.db import models

# Create your models here.

class Homes(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='homes',null=True,blank=True)

    class Meta:
        ordering=('name',)
        
        
    def __str__(self):
        return self.name




class Testimo(models.Model):
    name=models.CharField(max_length=50)
    detail=models.CharField(max_length=250)
    place=models.CharField(max_length=100)

        
    def __str__(self):
        return self.name





class Enquery(models.Model):
    names=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    number=models.IntegerField(unique=True)
    message=models.CharField(max_length=300)
  
        
    def __str__(self):
        return self.names


class Appointment(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    phone=models.IntegerField(unique=True)
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=10)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=250)
    message=models.CharField(max_length=250)

    def __str__(self):
        return self.name




class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    phone=models.IntegerField(unique=True)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=250)
    
    def __str__(self):
        return self.name



class Branch(models.Model):
    image=models.ImageField(upload_to='branch')
    name=models.CharField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        
    def __str__(self):
        return self.name





class Gallery(models.Model):
    image=models.ImageField(upload_to='gallerys',blank=True)
    class Meta:
        ordering=('image',)
        
        
    def ImageField(self):
        return self.image




class Blog(models.Model):
    image=models.ImageField(upload_to='blog')
    name=models.CharField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        
    def __str__(self):
        return self.name



class Package(models.Model):
    image=models.ImageField(upload_to='package')
    price=models.IntegerField()
    ln1=models.CharField(max_length=400)
    ln2=models.CharField(max_length=400)
    ln3=models.CharField(max_length=400)
    ln4=models.CharField(max_length=400)
    ln5=models.CharField(max_length=400)
    ln6=models.CharField(max_length=400)
    ln7=models.CharField(max_length=400,blank=True)
    ln8=models.CharField(max_length=400,blank=True)
    ln9=models.CharField(max_length=400,blank=True)
    ln10=models.CharField(max_length=400,blank=True)
    ln11=models.CharField(max_length=400,blank=True)
    ln12=models.CharField(max_length=400,blank=True)
    ln13=models.CharField(max_length=400,blank=True)
    name=models.CharField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        
    def __str__(self):
        return self.name    



  
