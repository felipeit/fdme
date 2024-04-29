from src.findme.domain.phones.dto import PhoneBase



class Phone:
    def __init__(self, phone: PhoneBase) -> None:
        self.__id = phone.id
        self.__phone_number = phone.phone_number
        self.__imei = phone.imei
        self.__model = phone.model
        self.__os = phone.os
        self.__latitude = phone.latitude
        self.__longitude = phone.longitude
        self.__created_at = phone.created_at
        self.__updated_at = phone.updated_at
        self.__active = phone.active

    @property
    def latitude(self) -> float:
        return self.__latitude