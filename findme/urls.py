from django.urls import include, path
from rest_framework.routers import DefaultRouter

from findme.views import UserViewSet

router = DefaultRouter()

router.register("register_user", UserViewSet)


urlpatters = [
    path('', include(router.urls))
]