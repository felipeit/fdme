from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from src.findme.application.users_usecase.dto import Input
from src.findme.application.users_usecase.register_user import RegisterUser
from src.findme.infra.orm.models import User
from src.findme.infra.api.serializers import UserSerializer

class UserViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @extend_schema(
            parameters=[],
            request=UserSerializer
    )
    def create(self, request, *args, **kwargs) -> Response:
        input = Input(
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
        usecase = RegisterUser(user_db=User)
        output = usecase.execute(input)
        return Response(output, status=status.HTTP_201_CREATED)