from django.db import models

# Create your models here.
class Employee_data(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=20)
    email=models.EmailField()
    desig=models.CharField(max_length=20)