from dataclasses import dataclass, field
from typing import Any, Protocol
from uuid import UUID
from src.findme.domain.user import User
from src.findme.infra.orm.phone_models import Phone

@dataclass
class Input:
    id: Any = None
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    cpf: str = ""
    cnpj: str = ""
    address: str = ""
    phone_number: str = ""
    related_phone: Phone | None = None
    age: int = 0


@dataclass
class OutputSuccess:
    id: str | UUID


@dataclass
class OutputError:
    errors: list[str] = field(default_factory=list)


class UserDb(Protocol):  # Persiste
    def create_user(self, user: User) -> None:
        ...

class RegisterUser:
    def __init__(self, user_db: UserDb) -> None:
        self._db = user_db

    def execute(self, input: 'Input') -> OutputSuccess | OutputError:
        user = User(
            id=input.id,
            first_name=input.first_name,
            last_name=input.last_name,
            age=input.age,
            email=input.email,
            cpf=input.cpf,
            cnpj=input.cnpj,
            address=input.address,
            phone_number=input.phone_number,
            related_phone=input.related_phone,
        )
    
        self._db.create_user(user)
        return OutputSuccess(id=user.id)
    #return OutputError(errors=[str(e) for e in user.errors])