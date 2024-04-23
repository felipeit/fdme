from src.findme.application.users_usecase.dto import Input, OutputError, OutputSuccess, PreInput
from src.findme.domain.users.user import User



class PreRegisterUser:
    def execute(self, input: PreInput) -> OutputSuccess | OutputError:
        user = User(input)
        self._db.create_user(user)
        return OutputSuccess(id=user.id)
    #return OutputError(errors=[str(e) for e in user.errors])