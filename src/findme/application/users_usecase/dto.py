from dataclasses import dataclass, field
from uuid import UUID, uuid4
from src.findme.domain.phones.phone import Phone
from src.findme.domain.validation import PyValidatron, ValidationType


@dataclass
class Input:
    id: UUID
    first_name: str
    last_name: str
    email: str
    cpf: str
    cnpj: str
    address: str
    phone_number: str
    related_phone: Phone | None
    age: int

    def __post_init__(self) -> None:
        PyValidatron(value=self.first_name, type=ValidationType.STRING, min=1, max=100)
        PyValidatron(value=self.last_name, type=ValidationType.STRING, min=1, max=100)
        PyValidatron(value=self.email, type=ValidationType.EMAIL, min=1, max=100)
        PyValidatron(value=self.cpf, type=ValidationType.CPF, min=11, max=11)
        PyValidatron(value=self.address, type=ValidationType.STRING, min=1, max=100, blank=True)
        PyValidatron(value=self.phone_number, type=ValidationType.STRING, min=11, max=11, blank=True)
        PyValidatron(value=self.age, type=ValidationType.INT, min=1, max=100)

@dataclass
class PreInput:
    id: UUID
    first_name: str
    last_name: str
    email: str

    def __post_init__(self) -> None:
        PyValidatron(value=self.first_name, type=ValidationType.STRING, min=1, max=100)
        PyValidatron(value=self.last_name, type=ValidationType.STRING, min=1, max=100)
        PyValidatron(value=self.email, type=ValidationType.EMAIL, min=1, max=100)


@dataclass
class OutputSuccess:
    id: str | UUID


@dataclass
class OutputError:
    errors: list[str] = field(default_factory=list)