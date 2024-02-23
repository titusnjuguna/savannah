from django.db.models.signals import post_save
from datetime import datetime
from django.dispatch import receiver
from .models import Orders
from customers.models import Customers
from .function import send_message

@receiver(post_save,sender=Orders)
def send_order_details(sender,instance,created,**kwargs):
    # order = Orders.objects.id(id=instance.id)
    if created:
        api_key="eaa4d21f32a7a3f9cc9528b2e115c21944cb89e2d3d411b08bea9ed971263e4f"
        customerId = instance.customer_phone
        print(customerId)
        customer_details=Customers.objects.get(phone=customerId)
        phone = customer_details.phone
        fname = customer_details.first_name
        message = f'Dear+{fname}+your+order+has+been+created+successfully.Your+Order+ID+is+{instance.id}.'
        send_message(phone=phone,message=message,apikey=api_key,username="sandbox")
      
