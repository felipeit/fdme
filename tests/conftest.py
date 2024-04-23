import pytest
from uuid import uuid4

from channels.testing import WebsocketCommunicator
from src.findme.application.users_usecase.pre_register_user import Input
from src.findme.infra.websocket.consumers import GeolocationConsumer

# TODO: https://channels.readthedocs.io/en/latest/topics/testing.html
@pytest.fixture
async def user() -> Input:
    return Input(
        id=uuid4(),
        first_name="Elon",
        last_name="musk",
        email="test@test.com",
        cpf="98245952010",
        cnpj="99892490000145",
        address="Supremo Tribunal Federal",
        phone_number="6132173000",
        related_phone=None,
        age=18     
    )


@pytest.fixture
async def communicator_fixture() -> WebsocketCommunicator:
    return WebsocketCommunicator(GeolocationConsumer.as_asgi(), "/layer/")