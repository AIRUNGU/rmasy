from django.urls import path
from reporter import consumers as r_con

websocket_urlpatterns = [
    path('wss/report/<str:code>/', r_con.ReportPlatform),
]