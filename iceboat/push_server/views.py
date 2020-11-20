from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ImageData
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def get_image(request):
    if(request.method == 'POST'):
        image = request.FILES.get("image")
        name = request.POST.get('name')
        form = ImageData( image = image, name=name)
        form.save()
        print(image,name)
        render(request, '알림화면/push.html')
    return  JsonResponse({'code': '0000', 'msg': '이미지 받았습니다.'}, status=200)
