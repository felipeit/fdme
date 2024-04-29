
from src.findme.application.services.mediator import Dispatch
from src.findme.application.users_usecase.dto import OutputError, OutputSuccess, PreInput
from src.findme.domain.users.user import User
from src.findme.infra.orm.models import User as UserModel
from src.findme.infra.repository.user_repository import RegisterUserRepository
from src.findme.application.services.email_service import SendEmailActiveUserHandler



class PreRegisterUser:
    def __init__(self) -> None:
        self.repo = RegisterUserRepository(db=UserModel)

    @Dispatch(SendEmailActiveUserHandler())
    def execute(self, input: PreInput) -> OutputSuccess | OutputError:
        user = User(input)
        self.repo.pre_create_user(user)
        return OutputSuccess(id=user.id, events=user.get_events())