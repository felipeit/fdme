from typing import Any
from src.findme.domain.user import User
from src.findme.infra.orm.user_models import User as UserModel
from django.db import transaction

class RegisterUserRepository:
    def __init__(self, db: Any) -> None:
        self._db = db

    @transaction.atomic
    def create_user(self, user: User) -> None:
        self._db
        pass