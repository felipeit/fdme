from typing import Any, Literal

from .type_validate import ValidationType
from .base_validate import (
    validate_string,
    validate_email,
    validate_cpf,
    validate_integer,
)

class PyValidatron:
    """
    Inicializa uma instância de PyValidatron com os parâmetros de validação.

    Parâmetros:
        - type: Tipo de validação (ValidationType).
        - min: Valor mínimo permitido (deve ser menor que o máximo).
        - max: Valor máximo permitido (deve ser maior que o mínimo).
        - null: Indica se o valor pode ser nulo (opcional, default: False).
        - blank: Indica se o valor pode ser uma string vazia (opcional, default: False).
    """
    def __init__(self, value: Any, type: ValidationType, min: int, max: int, null: bool = False, blank: bool = False) -> None:
        self.value = value
        self.type = type
        self.min = min
        self.max = max
        self.null = null
        self.blank = blank
        self.exceptions = []
        
        self.valid()
    
    def valid(self) -> list[Any]:
        match self.type:
            case ValidationType.STRING:
                self.exceptions.append(
                    validate_string(value=self.value, min=self.min, max=self.max, blank=self.blank, null=self.null)
                )
            case ValidationType.EMAIL:
                self.exceptions.append(
                    validate_email(value=self.value, min=self.min, max=self.max, blank=self.blank, null=self.null)
                )
            case ValidationType.CPF:
                self.exceptions.append(
                    validate_cpf(value=self.value, min=self.min, max=self.max, blank=self.blank, null=self.null)
                )
            case ValidationType.INT:
                self.exceptions.append(
                    validate_integer(value=self.value, min=self.min, max=self.max, blank=self.blank, null=self.null)
                )
            case _:
                 raise ValueError("Type inexistente")
        return self.exceptions
    