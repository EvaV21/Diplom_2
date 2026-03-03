import allure


@allure.feature("Логин пользователя")
class TestLogin:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self, api, registered_user):
        r = api.login({"email": registered_user["email"], "password": registered_user["password"]})
        assert r.status_code == 200
        body = r.json()

        assert body.get("success") is True
        assert "accessToken" in body
        assert "refreshToken" in body

    @allure.title("Вход с неверным логином и паролем")
    def test_login_wrong_credentials(self, api):
        r = api.login({"email": "nope@yandex.ru", "password": "wrong"})
        assert r.status_code == 401
        body = r.json()

        assert body.get("success") is False
