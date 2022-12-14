from django.db import models

# Create your models here.

class Employee(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    DOB = models.DateField()
    DOJ = models.DateField()
    Department = models.CharField(max_length=80,null = True, blank=True)
    Post = models.CharField(max_length=50, null=True,blank=True)
    Address =  models.CharField(max_length=500 ,null=True,blank=True)
    City= models.CharField(max_length=50,null=True,blank=True)
    Country= models.CharField(max_length=50,null=True,blank=True)
    ZipCode = models.IntegerField(null=True,blank=True)
    State= models.CharField(max_length=50,null=True,blank=True)
    Active=models.BooleanField(null=True, default=True)
    Leave_count = models.IntegerField(null=True,blank=True)
    on_leave = models.BooleanField(null=True, default=False)

