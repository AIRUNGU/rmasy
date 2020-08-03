from django.urls import path
from reporter import views as r_views
urlpatterns = [
    path('home/', r_views.HomeP,name='home'),
]