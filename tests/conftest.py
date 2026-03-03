import pytest
import allure

from src.api import StellarApi
from src.helpers import generate_user


@pytest.fixture
def api():
    return StellarApi()


@pytest.fixture
def user_data():
    return generate_user()


@pytest.fixture
def registered_user(api, user_data):
    with allure.step("Регистрируем пользователя"):
        r = api.register(user_data)
    assert r.status_code == 200, f"register failed: {r.status_code} {r.text}"
    return user_data


@pytest.fixture
def token(api, registered_user):
    with allure.step("Логинимся и получаем токен"):
        r = api.login({"email": registered_user["email"], "password": registered_user["password"]})
    assert r.status_code == 200, f"login failed: {r.status_code} {r.text}"
    body = r.json()
    return body["accessToken"]  


@pytest.fixture
def ingredient_ids(api):
    with allure.step("Получаем список ингредиентов"):
        r = api.get_ingredients()
    assert r.status_code == 200, f"ingredients failed: {r.status_code} {r.text}"
    ids = [i["_id"] for i in r.json()["data"]]
    assert len(ids) > 1
    return ids[:2]