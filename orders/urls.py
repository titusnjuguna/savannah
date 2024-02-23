from django.urls import path, include
from . import views,function

urlpatterns=[
    path('create',views.create_order,name='createOrder'),
    path('items/<int:id>',views.get_order,name='order'),
    path('send',function.send_message,name='hj')
]