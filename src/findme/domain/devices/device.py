
from src.findme.domain.devices.dto import DeviceBase


class Device:
    def __init__(self, device: DeviceBase) -> None:
        self.__latitude = device.latitude
        self.__longitude = device.longitude