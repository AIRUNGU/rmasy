from django.urls import path
from reporter import consumers

websocket_urlpatterns = [
	path('wss/report/<str:room_name>/', consumers.ChatConsumer),
]