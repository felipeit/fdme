from typing import Any
from django.forms import ValidationError
from src.findme.domain.users.dto import UserBase


class User:
    def __init__(self, user: UserBase) -> None:
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
    def age(self) -> int:
        return self.__age
    
    @age.setter
    def age(self, value: int) -> None:
        if value < 18:
            raise ValidationError("Idade não permitida")
        self.__age = value 

    @property
    def full_name(self) -> str:
        return f"{self.__first_name} {self.__last_name}"
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    @cpf.setter
    def cpf(self, value: str) -> None:
        if not len(value) == 11:
            raise ValidationError("CPF invalído")
        self.__cpf = value

    @property
    def cnpj(self) -> str:
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, value: str) -> None:
        if not len(value) == 14:
            raise ValidationError("CNPJ invalído")
        self.__cnpj = value
    
    @property
    def email(self) -> None:
        return self.__email
    
    @email.setter
    def email(self, value: str) -> None:
        if not '@' in value:
            raise ValidationError("Email invalído")
        self.__email = value
