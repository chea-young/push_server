from django.urls import path
from . import views

app_name = 'quickstart'

urlpatterns = [
    path('alarm/', views.push_alarm),

]