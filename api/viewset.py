from rest_framework import viewsets
from api.serializes import UsuarioSerializer, SearchSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model
User = get_user_model()


class UsuarioViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UsuarioSerializer


@api_view(['GET'])
def user_filter(request, username):
	dados = User.objects.filter(username=username)
	serializer = SearchSerializer(dados, many=True)

	return Response(serializer.data)
