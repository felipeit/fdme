from django.urls import path

from src.findme.infra.websocket.consumers import GeolocationConsumer

websocket_urlpatterns = [path('layer/', GeolocationConsumer().as_asgi())]
