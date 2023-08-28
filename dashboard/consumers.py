import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class ECGConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "ecg",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "ecg",
            self.channel_name
        )

    async def receive(self, text_data):
      
        await self.channel_layer.group_send(
            "ecg",
            {
                'type': 'send.data',
                'data': text_data
            }
          
        )
        print(text_data)

    async def send_data(self, event):
        data = event['data']
        await self.send(json.dumps({'data': data}))

