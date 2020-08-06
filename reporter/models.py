from django.db import models
from djgeojson.fields import PointField
from leaflet.forms.widgets import LeafletWidget

# Create your models here.
class RealMapping(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pop = models.CharField(max_length=100)
    geom = PointField()

    def __str__(self):
        return self.pop