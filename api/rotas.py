from api import viewset
from rest_framework import routers

from django.contrib.auth import get_user_model
User = get_user_model()


router = routers.DefaultRouter()
router.register(r'users', viewset.UsuarioViewSet, base_name='User')
