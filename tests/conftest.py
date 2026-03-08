import pytest
import allure

from src.helpers import generate_user
from src.api import StellarApi


@pytest.fixture
def api():
    return StellarApi()


@pytest.fixture
def registered_user(api):
    user = generate_user()

    with allure.step("Регистрируем пользователя"):
        response = api.register(user)

    access_token = None
    if response.status_code == 200:
        body = response.json()
        access_token = body.get("accessToken")

    user_with_meta = {
        "email": user["email"],
        "password": user["password"],
        "name": user["name"],
        "response": response,
        "access_token": access_token,
    }

    yield user_with_meta

    if access_token: 
        with allure.step("Удаляем пользователя после теста"):
            api.delete_user(access_token)


@pytest.fixture
def token(api, registered_user):
    with allure.step("Логинимся и получаем токен"):
        response = api.login(
            {
                "email": registered_user["email"],
                "password": registered_user["password"],
            }
        )

    access_token = None
    if response.status_code == 200:
        body = response.json()
        access_token = body.get("accessToken")

    return {
        "response": response,
        "access_token": access_token,
    }


@pytest.fixture
def ingredient_ids(api):
    with allure.step("Получаем список ингредиентов"):
        response = api.get_ingredients()

    ids = []
    if response.status_code == 200:
        body = response.json()
        data = body.get("data", [])
        ids = [item["_id"] for item in data]

    return {
        "response": response,
        "ids": ids,
    }