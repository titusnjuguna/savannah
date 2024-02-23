from django.shortcuts import render
from .serializers import OrderSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Orders
from .function import send_message
from rest_framework.response import Response
import json
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND)
# Create your views here.
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        items = serializer.data.get('order_items')
        delivery= serializer.data.get('delivery_address')
        customer = serializer.data.get('customer_phone')
        items = json.dumps(items)
        Orders.objects.create(
            order_items=items,
            delivery_address=delivery,
            customer_phone=customer
        )
        
        return Response({'message':'Order Created successfully','code':HTTP_200_OK},status=HTTP_200_OK)
    
    return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_orders(request):
    orders = Orders.objects.all().order_by("-id")
    serializer = OrderSerializer(orders,many=True)
    return Response({'message':'Successful','data':serializer.data,'code':HTTP_200_OK},status=HTTP_200_OK)


@api_view(['GET'])
def get_order(request,id):
    order = Orders.objects.get(id=id)
    serializer=OrderSerializer(order)
    return Response({'message':'Successful','data':serializer.data,'code':HTTP_200_OK},status=HTTP_200_OK)

