from dataclasses import dataclass
from typing import Any
from findme.domain.errors_mixin import ErrorsMixin
from car_park.domain.value_objects.string import String


@dataclass
class User(ErrorsMixin):  # Valida as regras de negócio -> DOMAIN DDD
    email: str
    age: int
    first_name: str | String = String(
        min=3, max=20, field_name="first_name"
    )  # VALUE OBJECT DDD
    last_name: str | String = String(
        min=3, max=20, field_name="last_name"
    )  # VALUE OBJECT DDD
    id: Any = None

    def __post_init__(self) -> None:
        self.age = int(self.age)