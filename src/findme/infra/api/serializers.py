from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    cpf = serializers.CharField()
    cnpj = serializers.CharField()
    address = serializers.CharField()
    phone_number = serializers.CharField()
    related_phone = serializers.CharField()
    age = serializers.IntegerField()

class PreUserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
