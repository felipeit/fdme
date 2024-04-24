from typing import Union
from uuid import UUID
from django.forms import ValidationError
from src.findme.domain.users.dto import PreUserBase, UserBase


class User:
    def __init__(self, user: Union[UserBase, PreUserBase]) -> None:
        self.__id = user.id
        self.__first_name = user.first_name
        self.__last_name = user.last_name
        self.__email = user.email
        self.__cpf = getattr(user, 'cpf', None)
        self.__cnpj = getattr(user, 'cnpj', None)
        self.__address = getattr(user, 'address', None)
        self.__phone_number = getattr(user, 'phone_number', None)
        self.__related_phone = getattr(user, 'related_phone', None)
        self.__age = getattr(user, 'age', None)

        # Validações adicionais
        if hasattr(user, 'age') and user.age < 18:
            raise ValidationError("Idade não permitida")

        if hasattr(user, 'cpf') and len(user.cpf) != 11:
            raise ValidationError("CPF inválido")

        if hasattr(user, 'cnpj') and len(user.cnpj) != 14:
            raise ValidationError("CNPJ inválido")

        if hasattr(user, 'email') and '@' not in user.email:
            raise ValidationError("Email inválido")
        
    @property
    def id(self) -> UUID:
        return self.__id
    
    @property
    def age(self) -> int:
        return self.__age
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @property
    def full_name(self) -> str:
        return f"{self.__first_name} {self.__last_name}"

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @property
    def email(self) -> str:
        return self.__email
