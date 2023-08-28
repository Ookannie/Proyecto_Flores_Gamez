from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from dashboard import consumers

websocket_urlpatterns = [
    path('ws/ecg/', consumers.ECGConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})
