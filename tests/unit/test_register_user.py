import pytest
from django.forms import ValidationError
from src.findme.domain.user import User

#from src.findme.application.register_user import Input


async def test_user_with_age_minor_that_18(user) -> None:
    # arrange
    uc = User(user)
    # act & assert
    with pytest.raises(ValidationError):
        uc.age = 17

async def test_user_with_age_greater_that_18(user) -> None:
    # arrange
    uc = User(user)
    # act
    uc.age = 19
    # assert
    assert uc.age == 19
    
async def test_user_with_cpf_minor_that_11(user) -> None:
    # arrange
    uc = User(user)
    # act & assert
    with pytest.raises(ValidationError):
        uc.cpf = "1234567891"

async def test_user_with_cpf_greater_that_11(user) -> None:
    # arrange
    uc = User(user)
    # act & assert
    with pytest.raises(ValidationError):
        uc.cpf = "1234567891011"

async def test_user_with_cnpj_minor_that_14(user) -> None:
    # arrange
    uc = User(user)
    # act & assert
    with pytest.raises(ValidationError):
        uc.cnpj = "1234567891011"
    
async def test_user_with_cnpj_greater_that_14(user) -> None:
    # arrange
    uc = User(user)
    # act & assert
    with pytest.raises(ValidationError):
        uc.cnpj = "1234567891011121314"

async def test_user_with_email_wrong(user) -> None:
    # arrange
    uc = User(user)
    # act & assert
    with pytest.raises(ValidationError):
        uc.email = "testtest.com"
