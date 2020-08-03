from django.urls import path
from . import consumer

websocket_urlpatterns = [
	path('ws/report/<str:room_name>)/', consumer.ChatConsumer),
]