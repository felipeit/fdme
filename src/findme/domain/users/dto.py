from pydantic import BaseModel
from uuid import UUID

from src.findme.domain.phones.dto import PhoneBase


class UserBase(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    cpf: str
    cnpj: str
    address: str
    phone_number: str
    related_phone: PhoneBase | None
    age: int


class PreUserBase(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
