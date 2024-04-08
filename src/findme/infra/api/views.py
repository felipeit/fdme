from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, status
from rest_framework.response import Response

from src.findme.application.register_user import Input, RegisterUser
from src.findme.infra.api.models import User

class UserViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = None
    permission_classes = (IsAuthenticated,)

    async def create(self, request, *args, **kwargs) -> Response:
        input = Input(
            id=request.data.get('id'),
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            email=request.data.get('email'),
            age=request.data.get('age'),
            cpf=request.data.get('cpf'),
            cnpj=request.data.get('cnpj'),
            address=request.data.get('address'),
            phone_number=request.data.get('phone_number'),
            related_phone=request.data.get('related_phone')
        )
        data = RegisterUser(input)
        return Response(data, status=status.HTTP_201_CREATED)