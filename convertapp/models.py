from django.db import models

# Create your models here.
class files(models.Model):
    req=models.IntegerField(primary_key=True,default=0)
    fl=models.FileField()
    dt=models.DateTimeField(auto_now_add=True)
class reqtno(models.Model):
    requestnumber=models.IntegerField(primary_key=True,default=0)
class videofiles(models.Model):
    req=models.IntegerField(primary_key=True,default=0)
    fl=models.FileField()
    otformat=models.CharField(max_length=5,default=".mp3")
    dt=models.DateTimeField(auto_now_add=True)
    
    