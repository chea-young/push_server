from django.urls import path
from . import views

app_name = 'quickstart'

urlpatterns = [
    path('alarm/', views.push_alarm),
    path('send/', views.send),
    path('azure', views.azure)

]