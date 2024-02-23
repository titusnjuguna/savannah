from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone =  models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)


