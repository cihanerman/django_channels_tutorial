from django.urls import path, include
from .views import *

app_name = 'chat'

urlpatterns = [
    path('', index, name='index'),
    path('<room_name>/', room, name='room'),
]