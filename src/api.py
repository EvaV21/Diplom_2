import allure
import requests

from src.config import BASE_URL, REGISTER, LOGIN, INGREDIENTS, ORDERS, USER


class StellarApi:
    def __init__(self):
        self.session = requests.Session()

    @allure.step("POST {path}")
    def post(self, path: str, json: dict | None = None, headers: dict | None = None):
        return self.session.post(BASE_URL + path, json=json, headers=headers)

    @allure.step("GET {path}")
    def get(self, path: str, headers: dict | None = None):
        return self.session.get(BASE_URL + path, headers=headers)

    @allure.step("DELETE {path}")
    def delete(self, path: str, headers: dict | None = None):
        return self.session.delete(BASE_URL + path, headers=headers)

    @allure.step("Зарегистрировать пользователя")
    def register(self, payload: dict):
        return self.post(REGISTER, json=payload)

    @allure.step("Выполнить логин пользователя")
    def login(self, payload: dict):
        return self.post(LOGIN, json=payload)

    @allure.step("Получить список ингредиентов")
    def get_ingredients(self):
        return self.get(INGREDIENTS)

    @allure.step("Создать заказ")
    def create_order(self, ingredients: list[str] | None = None, token: str | None = None):
        headers = {"Authorization": token} if token else None
        body = {"ingredients": ingredients} if ingredients is not None else {}
        return self.post(ORDERS, json=body, headers=headers)

    @allure.step("Удалить пользователя")
    def delete_user(self, token: str):
        headers = {"Authorization": token}
        return self.delete(USER, headers=headers)