from dataclasses import asdict, dataclass, field
from typing import Protocol
from uuid import UUID
from findme.domain.user import User

@dataclass
class Input:  # DTO - Data Transfer Object
    first_name: str
    last_name: str
    email: str
    age: int


@dataclass
class OutputSucess:  # DTO - Data Transfer Object
    id: str | UUID


@dataclass
class OutputError:  # DTO - Data Transfer Object
    errors: list[str] = field(default_factory=list)


class UserDb(Protocol):  # Persiste
    def create_user(self, user: User) -> None:
        ...

class RegisterUser:
    def __init__(self, user_db: UserDb) -> None:
        self._db = user_db

    def execute(self, input: Input) -> OutputSucess | OutputError:
        user = User(
            email=input.email,
            age=input.age,
            first_name=input.first_name,
            last_name=input.last_name,
        )
        if not user.errors:
            self._db.create_user(user)
            return OutputSucess(id=user.id)
        return OutputError(errors=[str(e) for e in user.errors])