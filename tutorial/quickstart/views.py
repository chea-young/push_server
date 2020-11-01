from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets,status,generics
from .serializers import UserSerializer, GroupSerializer
from pyfcm import FCMNotification
import requests
import json
from firebase_admin import messaging
import firebase_admin

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def push_alarm(request):
    context = {'text' : 'Check!!'}
    #send_to()
    return render(request, 'quickstart/push_alarm.html',context)

def send_to_fcm(ids, title, body):
    url = 'https://fcm.googleapis.com/fcm/send'
    headers = {
        'Authorization': 'key=AAAAZcj4Rbw:APA91bFK6p_oAAVMFlEUo3hfvdYY3pQS-8gTc3C8nkDl7OHRgsxMp3PDnkH7tY__tU1tKNXu-etFUGn9n_cOu5ElsSpw8x-Iy1j7Jxr9kgZgdZjRCXwB6bVXlyVkhqPAeNMyzPBEUDZF',
        'Content-Type': 'application/json; UTF-8',
    }
    content = {
        "registration_ids":ids,
        'notification': {
            'title': title,
            'body': body
        }
    }
    requests.post(url, data=json.dumps(content), headers=headers)
    
def send(request):
    send_to_token()
    key = 'BKCS4dNROfKjEcGimv6mI10sR_vmOvbRwmgWmVd249-i4ohjxuM6OrXCuLebnJmYL_8FaMVQyM3cdddXhwFuL9k'
    send_to_fcm(key, 'Hi', 'By')
    return render(request, 'quickstart/send.html')

def send_to_token():
    default_app = firebase_admin.initialize_app()
    registration_tokens = [
        'BKCS4dNROfKjEcGimv6mI10sR_vmOvbRwmgWmVd249-i4ohjxuM6OrXCuLebnJmYL_8FaMVQyM3cdddXhwFuL9k',
    ]

    message = messaging.MulticastMessage(
        data={'score': '850', 'time': '2:45'},
        tokens=registration_tokens,
    )
    response = messaging.send_multicast(message)
    if response.failure_count > 0:
        responses = response.responses
        failed_tokens = []
        for idx, resp in enumerate(responses):
            if not resp.success:
                # The order of responses corresponds to the order of the registration tokens.
                failed_tokens.append(registration_tokens[idx])
        print('List of tokens that caused failures: {0}'.format(failed_tokens))



