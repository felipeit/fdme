"""
ASGI config for zoomrural project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from src.findme.infra.websocket.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.core.settings')
app = get_asgi_application()

# from src.findme.infra.websocket.channels_middleware import AuthMiddlewareStack #JwtAuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter  # noqa isort:skip

application = ProtocolTypeRouter(
    {
        'http': app,
        #'websocket': AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
        'websocket': URLRouter(websocket_urlpatterns),
    }
)
