from typing import Any
from src.findme.application.users_usecase.dto import Input, OutputError, OutputSuccess
from src.findme.domain.users.user import User

class RegisterUser:
    def execute(self, input: Input) -> OutputError | OutputSuccess:
        user = User(input=input)
        self._db.create_user(user)
        return OutputSuccess(id=user.id)
    #return OutputError(errors=[str(e) for e in user.errors])