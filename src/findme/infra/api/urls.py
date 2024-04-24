from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.findme.infra.api.views import PreUserViewSet, UserViewSet

router = DefaultRouter()

router.register("register_user", UserViewSet, basename="fully_registered_user")
router.register("pre_register", PreUserViewSet, basename="partially_registered_user")


urlpatters = [
    path('', include(router.urls))
]