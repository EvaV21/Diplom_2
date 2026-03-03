import allure
import pytest


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создать уникального пользователя")
    def test_create_unique_user(self, api, user_data):
        r = api.register(user_data)
        assert r.status_code == 200
        body = r.json()

        assert body.get("success") is True
        assert "accessToken" in body
        assert "refreshToken" in body
        assert body["user"]["email"] == user_data["email"]

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, api, registered_user):
        r = api.register(registered_user)
        assert r.status_code == 403
        body = r.json()

        assert body.get("success") is False
        assert "User already exists" in body.get("message", "")

    @allure.title("Создать пользователя без обязательного поля")
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_create_user_missing_required_field(self, api, user_data, field):
        payload = dict(user_data)
        payload.pop(field)

        r = api.register(payload)
        assert r.status_code == 403
        body = r.json()

        assert body.get("success") is False