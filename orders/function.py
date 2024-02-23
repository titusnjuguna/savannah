import requests
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND)

def send_message(phone,message,apikey,username):
    url = "https://api.sandbox.africastalking.com/version1/messaging"
    sender = "AFRICASTKNG"
    payload = "username="+username+"&to="+phone+"&message="+message
    # +"&from="+sender
    headers = {'apiKey': apikey,'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, headers=headers, data=payload)
    return Response({'message':'Succ','reponse':response},status=HTTP_200_OK)