from dataclasses import dataclass
from datetime import datetime
from src.findme.domain.user import User


@dataclass
class PhoneBase:
    id: str
    phone_number: str
    imei: str
    model: str
    os: str
    user: User
    latitude: float
    longitude: float
    created_at: datetime
    updated_at: datetime
    active: bool


class Phone:
    async def __init__(self, phone: PhoneBase) -> None:
        self.__id = phone.id
        self.__phone_number = phone.phone_number
        self.__imei = phone.imei
        self.__model = phone.model
        self.__os = phone.os
        self.__user = phone.user
        self.__latitude = phone.latitude
        self.__longitude = phone.longitude
        self.__created_at = phone.created_at
        self.__updated_at = phone.updated_at
        self.__active = phone.active

    @property
    async def latitude(self) -> float:
        return self.__latitude