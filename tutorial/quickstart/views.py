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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def send_to():
    registration_ids = "BKCS4dNROfKjEcGimv6mI10sR_vmOvbRwmgWmVd249-i4ohjxuM6OrXCuLebnJmYL_8FaMVQyM3cdddXhwFuL9k"
    message = messaging.Message(
    notification=messaging.Notification(
        title='안녕하세요 타이틀 입니다',
        body='안녕하세요 메세지 입니다',
    ),
    token=registration_ids,
    )
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)

def push_alarm(request):
    context = {'text' : 'Check!!'}
    #send_to()
    key = 'BKCS4dNROfKjEcGimv6mI10sR_vmOvbRwmgWmVd249-i4ohjxuM6OrXCuLebnJmYL_8FaMVQyM3cdddXhwFuL9k'
    send_to_fcm(key, 'Hi', 'By')
    return render(request, 'quickstart/index.html',context)

def send_fcm_notification(ids, title, body):
    url = 'https://fcm.googleapis.com/fcm/send'# fcm 푸시 메세지 요청 주소
    # 인증 정보(서버 키)를 헤더에 담아 전달
    headers = {
        'Authorization': 'key=AAAAZcj4Rbw:APA91bFK6p_oAAVMFlEUo3hfvdYY3pQS-8gTc3C8nkDl7OHRgsxMp3PDnkH7tY__tU1tKNXu-etFUGn9n_cOu5ElsSpw8x-Iy1j7Jxr9kgZgdZjRCXwB6bVXlyVkhqPAeNMyzPBEUDZF',
        'Content-Type': 'application/json; UTF-8',
    }
    # 보낼 내용과 대상을 지정
    #registration_ids는 단일 대상일 때 여러명이면 배열로 1000개까지 가능
    content = {
        'registration_ids': ids,
        'notification': {
            'title': title,
            'body': body
        }
    }
    requests.post(url, data=json.dumps(content), headers=headers) # json 파싱 후 requests 모듈로 FCM 서버에 요청

def send_to_fcm(ids, title, body):
    url = 'https://fcm.googleapis.com/fcm/send'

    headers = {
        'Authorization': 'key=AAAAZcj4Rbw:APA91bFK6p_oAAVMFlEUo3hfvdYY3pQS-8gTc3C8nkDl7OHRgsxMp3PDnkH7tY__tU1tKNXu-etFUGn9n_cOu5ElsSpw8x-Iy1j7Jxr9kgZgdZjRCXwB6bVXlyVkhqPAeNMyzPBEUDZF',
        'Content-Type': 'application/json; UTF-8',
    }
    # See documentation on defining a message payload.
    content = {
        "registration_ids":ids,
        'notification': {
            'title': title,
            'body': body
        }
    }
    requests.post(url, data=json.dumps(content), headers=headers)
    #return render(request, 'quickstart/send.html',context)



