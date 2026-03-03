import allure
import requests

from src.config import BASE_URL, REGISTER, LOGIN, INGREDIENTS, ORDERS


class StellarApi:
    def __init__(self):
        self.session = requests.Session()

    @allure.step("POST {path}")
    def post(self, path: str, json: dict | None = None, headers: dict | None = None):
        return self.session.post(BASE_URL + path, json=json, headers=headers)

    @allure.step("GET {path}")
    def get(self, path: str, headers: dict | None = None):
        return self.session.get(BASE_URL + path, headers=headers)

    def register(self, payload: dict):
        return self.post(REGISTER, json=payload)

    def login(self, payload: dict):
        return self.post(LOGIN, json=payload)

    def get_ingredients(self):
        return self.get(INGREDIENTS)

    def create_order(self, ingredients: list[str] | None = None, token: str | None = None):
        headers = {"Authorization": token} if token else None
        body = {"ingredients": ingredients} if ingredients is not None else {}
        return self.post(ORDERS, json=body, headers=headers)