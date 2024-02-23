from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase,APIClient

from customers.models import * 
from customers.views import *  

client = APIClient()
class YourViewTest(APITestCase):
    def test_get_list(self):
        response = client.get(reverse('allcustomers'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_create_item(self):
        # Prepare the data to create
        data = {
            "first_name":"Abel",
            "last_name":"Mutua",
            "phone":'254708520548',
            "delivery_address":"Mirema Drive"
        }
        response = client.post(reverse('createCustomers'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_create_order(self):
        data={
            "order_items":[{"item":"2 pair Trouser","price":"2000","quantity":"3"}],
            "delivery_address":"Kianjukuma",
            "customer_phone":254708520548
        }
        response= client.post(reverse('createOrder'),data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
   

