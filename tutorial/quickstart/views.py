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
    #send_pushserver()
    send_to_token()
    return render(request, 'quickstart/push_alarm.html',context)

def send_to(ids, title, body):
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
    key = 'BKCS4dNROfKjEcGimv6mI10sR_vmOvbRwmgWmVd249-i4ohjxuM6OrXCuLebnJmYL_8FaMVQyM3cdddXhwFuL9k'
    send_to_fcm(key, 'Hi', 'By')
    return render(request, 'quickstart/send.html')

def send_to_token():
    #default_app = firebase_admin.initialize_app()
    registration_tokens ='BNe0FkSflOmQ7Fbqy9tymAl0-7W8GpJXdiQ9wal0BUPrMDMP--DVNWkhF8Bhy6CXlPsSNkY1zoNOXsnTacPzF-8'
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token=registration_tokens,
    )
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)

def send_pushserver():
    # This registration token comes from the client FCM SDKs.
    registration_token = 'BNe0FkSflOmQ7Fbqy9tymAl0-7W8GpJXdiQ9wal0BUPrMDMP--DVNWkhF8Bhy6CXlPsSNkY1zoNOXsnTacPzF-8'
    # See documentation on defining a message payload.
    message = messaging.Message(
    notification=messaging.Notification(
        title='안녕하세요 타이틀 입니다',
        body='안녕하세요 메세지 입니다',
    ),
    token='BNe0FkSflOmQ7Fbqy9tymAl0-7W8GpJXdiQ9wal0BUPrMDMP--DVNWkhF8Bhy6CXlPsSNkY1zoNOXsnTacPzF-8',
    )
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)

