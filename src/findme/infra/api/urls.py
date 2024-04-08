from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.findme.infra.api.views import UserViewSet

router = DefaultRouter()

router.register("register_user", UserViewSet)


urlpatters = [
    path('', include(router.urls))
]