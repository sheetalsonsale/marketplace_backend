from django.db import models

# Create your models here.
class customer(models.Model):
    username = models.CharField(max_length=32,unique=True,)
    password = models.CharField(max_length=32,default='123456')
    email = models.EmailField(max_length=32,unique=True)
    name = models.CharField(max_length=32,null=True,blank=True)
    gender = models.CharField(
        max_length=10, choices=[('m', 'Male'), ('f', 'Female')]
    )  

    def __str__(self):
        return self.name