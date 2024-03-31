from django.urls import path

from findme.infra.websocket.consumers import GeolocationConsumer

websocket_urlpatterns = [path('operacao/', GeolocationConsumer.as_asgi())]
