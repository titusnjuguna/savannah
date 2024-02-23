from django.db import models
from customers.models import Customers

# Create your models here.
class Orders(models.Model):
    order_items = models.JSONField(default=list)
    delivery_address = models.CharField(max_length=100,null=True,blank=True)
    customer_phone = models.CharField(max_length=100,null=True,blank=True)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)