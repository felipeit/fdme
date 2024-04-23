import re


def validate_string(value: str, min: int, max: int, blank: bool, null) -> None:
    if min > max:
        return ValueError("O valor mínimo não pode ser maior que o valor máximo.")
    if not blank and value == "":
        return ValueError("O valor não pode ser em branco.")
    if not null and value == None:
        return ValueError("O valor não pode ser nulo.")
    if len(value) > max:
        return ValueError("Valor maior que o permitido.")
    if len(value) < min:
        return ValueError("Valor menor que o permitido.")

def validate_email(value: str, min: int, max: int, blank: bool, null) -> None:
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, value):
        return ValueError("email fora do padrão permitido")

def validate_cpf(value: str, min: int, max: int, blank: bool, null) -> None:...

def validate_integer(value: str, min: int, max: int, blank: bool, null) -> None:
    if len(value) > max:
        return ValueError("Valor maior que o permitido.")
    if len(value) < min:
        return ValueError("Valor menor que o permitido.")