from typing import Any

from attr import asdict
from src.findme.domain.users.user import User
from src.findme.infra.orm.models import User as UserModel
from django.db import transaction

class RegisterUserRepository:
    def __init__(self, db: UserModel) -> None:
        self._db = db

    @transaction.atomic
    def pre_create_user(self, user: User) -> None:
        self._db.objects.create(
            id=user.id,
            first_name=user.first_name, 
            last_name=user.last_name, 
            email=user.email
        )
        
