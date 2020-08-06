from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer
from reporter import models as r_models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry
import json

class ReportPlatform(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['code']
        self.user = self.scope["user"]
        self.room_group_name = 'report_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        data1 = text_data_json['data1']
        self._save_to_db(data1)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'report_message',
                'data1':data1
            }
        )

    def report_message(self,event):
        data1 = event['data1']
        self.send(text_data=json.dumps({
            'data1':data1
        }))

    
    def _save_to_db(self,indata):
        lat = indata['lat']
        lon = indata['lon']
        pop = indata['popmsg']
        geom = {
              
                "type": "Point",
                "coordinates": [float(lon), float(lat)]
            }
        geo_model = r_models.RealMapping.objects.create(lat=lat,lon=lon,pop=pop,geom=geom)
        
        return geo_model

    def _retrieve_from_db(self):
        geodata = r_models.RealMapping.objects.all()
        return geodata
        
    