from typing import Any
# from channels.db import database_sync_to_async
# from channels.sessions import CookieMiddleware, SessionMiddleware
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# from rest_framework_simplejwt.tokens import UntypedToken
# from channels.middleware import BaseMiddleware
# from channels.auth import AuthMiddleware, AuthMiddlewareStack
# from django.db import close_old_connections
# from urllib.parse import parse_qs
# from jwt import decode as jwt_decode


# @database_sync_to_async
# def get_user(id, domain):
#     return get_user_model().objects.get(id=id)


# class JwtAuthMiddleware(BaseMiddleware):...
#     async def __init__(self, inner) -> None:
#         self.inner = inner

#     async def __call__(self, scope, receive, send) -> None:
#         # Close old database connections to prevent usage of timed out connections
#         close_old_connections()

#         # Get the token
#         token = parse_qs(scope['query_string'].decode('utf8'))['token'][0]

#         try:
#             UntypedToken(token)
#         except (InvalidToken, TokenError) as e:
#             print(e)
#             return None
#         else:
#             decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#             print(decoded_data)
#             # Will return a dictionary like -
#             # {
#             #     "token_type": "access",
#             #     "exp": 1568770772,
#             #     "jti": "5c15e80d65b04c20ad34d77b6703251b",
#             #     "user_id": 6
#             # }

#             # Get the user using ID
#             host = ''
#             for header in scope.get('headers'):
#                 if (header[0].decode('utf8')) == 'host':
#                     host = header[1].decode('utf8')
#             scope['user'] = await get_user(decoded_data['user_id'], host.split(':')[0])

#         return await super().__call__(scope, receive, send)


# def JwtAuthMiddlewareStack(inner) -> JwtAuthMiddleware:
#     return JwtAuthMiddleware(AuthMiddlewareStack(inner))

# from django.core.asgi import get_asgi_application
# from django.urls import re_path

# from src.findme.infra.websocket.consumers import GeolocationConsumer

# # # Initialize Django ASGI application early to ensure the AppRegistry
# # # is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()

# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator
# from routing import websocket_urlpatterns


# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter([
#                 re_path(r"", websocket_urlpatterns.url),
#             ])
#         )
#     ),
# })
