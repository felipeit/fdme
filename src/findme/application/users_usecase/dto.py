from typing import Any
from pydantic import BaseModel
from dataclasses import field
from uuid import UUID
from src.findme.domain.events.dto import GenericEvent
from src.findme.domain.phones.dto import PhoneBase




class Input(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    cpf: str
    cnpj: str
    address: str
    phone_number: str
    related_phone: PhoneBase
    age: int


class PreInput(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str

class OutputSuccess(BaseModel):
    id: str | UUID
    events: Any #list[GenericEvent] = field(default_factory=list)


class OutputError(BaseModel):
    errors: list[str] = field(default_factory=list)
    events: list[GenericEvent] = field(default_factory=list)