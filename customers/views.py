from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import Customers
from .serializers import CustomerSerializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_201_CREATED,
                                    HTTP_404_NOT_FOUND)
import requests



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_customer(request):
    serializer = CustomerSerializers(data=request.data)
    if serializer.is_valid():
        fname = serializer.data.get('first_name')
        lname = serializer.data.get('last_name')
        phone = serializer.data.get('phone')
        delivery = serializer.data.get('delivery_address')

        #check if the number exist
        try:
            customer = Customers.objects.get(phone=phone)
            if customer:
                return Response({'message':'Customer with the number already Exist','code':HTTP_400_BAD_REQUEST},status=HTTP_400_BAD_REQUEST)
        except:
            Customers.objects.create(
                 first_name=fname,
                 last_name=lname,
                 phone=phone,
                 delivery_address=delivery
             )
            return Response({'message':'Customer Created successfully','code':HTTP_201_CREATED},status=HTTP_201_CREATED)
    return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_customers(request):
    all_customers =  Customers.objects.all()
    serializer = CustomerSerializers(all_customers,many=True)
    return Response({'message':'Customer Created successfully','customers':serializer.data,'code':HTTP_200_OK},status=HTTP_200_OK)


def exchange_code_for_token(code):
    # Make a POST request to the OIDC provider's token endpoint to exchange the authorization code for an access token
    token_endpoint = 'http://localhost:8000/openid/token/'
    client_id = '100654'
    client_secret = '865407257fb31f1ac4e236b95f339b318cf7f2421fa6ac89daae29eb'
    redirect_uri = 'http://localhost:8000/api/v1/customers/callback'

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri
    }

    response = requests.post(token_endpoint, data=data)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        print(token_data)
        return access_token
    else:
        return None


def login(request):
    # Construct the URL to the OIDC provider's authorization endpoint
    authorization_endpoint = 'http:/localhost:8000/openid/authorize/'
    client_id =	'100654'
    redirect_uri = request.build_absolute_uri(reverse('callback'))
    scope ='openid profile email'  # Specify the scopes required by your application
    # Redirect the user to the OIDC provider's authorization endpoint
    redirect_url = f"{authorization_endpoint}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"
    return HttpResponseRedirect(redirect_url)

def callback(request):
    # Extract the authorization code from the request
    code = request.GET.get('code')
    if code:
        # Exchange the authorization code for an access token
        access_token = exchange_code_for_token(code)
        if access_token:
            # Handle successful authentication
            print(access_token)
            return HttpResponse({'token':access_token})
        else:
            # Handle error obtaining the access token
            print("None is token")
    else:
        # Handle missing authorization code
        pass
    return HttpResponse({})
