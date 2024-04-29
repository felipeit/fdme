from pydantic import BaseModel
from datetime import datetime


class PhoneBase(BaseModel):
    id: str
    phone_number: str
    imei: str
    model: str
    os: str
    latitude: float
    longitude: float
    created_at: datetime
    updated_at: datetime
    active: bool