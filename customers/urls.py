from django.urls import path, include
from . import views

urlpatterns=[
    path('create',views.create_customer,name='createCustomers'),
    path('all',views.get_customers,name='allcustomers'),
    path('login',views.login, name='login'),
    path('callback',views.callback,name='callback'),
]