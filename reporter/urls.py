from django.urls import path
from django.conf.urls import url
from reporter import views as r_views
from djgeojson.views import GeoJSONLayerView
from reporter import models as r_models

urlpatterns = [
    path('home', r_views.Prohome, name='home'),
    path('report/<str:code>/', r_views.Proreporter, name='code'),
    path('data.geojson', GeoJSONLayerView.as_view(model=r_models.RealMapping), name='data')
]