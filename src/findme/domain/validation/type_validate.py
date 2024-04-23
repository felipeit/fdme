from enum import Enum


class ValidationType(Enum):
    STRING = "string"
    EMAIL = "email"
    CPF = "cpf"
    INT = "int"