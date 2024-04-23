from dataclasses import dataclass
from datetime import datetime
from src.findme.domain.users.user import User


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