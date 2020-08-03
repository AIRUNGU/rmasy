from django.urls import path
from reporter import views as r_views
urlpatterns = [
    path('home/', r_views.HomeP,name='home'),
    path('report/<str:room_name>/', r_views.room, name='room_name'),
]