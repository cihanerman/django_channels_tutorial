# chat/routing.py
from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path('ws/chat/<room_name>/', ChatConsumer),
]