from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from findme.models import User

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = None
    permission_classes = (IsAuthenticated,)