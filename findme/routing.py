from django.urls import path

from findme.consumers import GeolocationConsumer

websocket_urlpatterns = [path('operacao/', GeolocationConsumer.as_asgi())]
