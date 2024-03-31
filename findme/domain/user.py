from typing import Any
from django.forms import ValidationError
# from findme.application.register_user import Input


class User:
    async def __int__(self, user: Any) -> None:
        self.__id = user.id
        self.__first_name = user.first_name
        self.__last_name = user.last_name
        self.__email = user.email
        self.__cpf = user.cpf
        self.__cnpj = user.cnpj
        self.__address = user.address
        self.__phone_number = user.phone_number
        self.__related_phone = user.related_phone
        self.__age = user.age

    @property
    async def age(self) -> int:
        return self.__age
    
    @age.setter
    async def age(self, value) -> None:
        if value < 18:
            raise ValidationError("Idade não permitida")
        self.__age = value 

    @property
    async def full_name(self) -> str:
        return f"{self.__first_name} {self.__last_name}"