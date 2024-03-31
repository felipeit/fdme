from dataclasses import dataclass


@dataclass
class DeviceBase:
    latitude: float
    longitude: float


class Device:
    def __init__(self, device: DeviceBase) -> None:
        self.__latitude = device.latitude
        self.__longitude = device.longitude