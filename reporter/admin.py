from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.forms.widgets import LeafletWidget
from reporter import models as r_models
# Register your models here.

class RealMappingAdmin(LeafletGeoAdmin):
    list_display = ['pop','lat','lon','geom']

    


admin.site.register(r_models.RealMapping,RealMappingAdmin)