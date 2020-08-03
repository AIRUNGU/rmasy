from django.urls import path
from reporter import consumers

websocket_urlpatterns = [
	path('ws/report/<str:room_name>/', consumers.ChatConsumer),
]