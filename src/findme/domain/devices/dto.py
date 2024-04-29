from pydantic import BaseModel


class DeviceBase(BaseModel):
    latitude: float
    longitude: float