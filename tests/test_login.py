import allure


@allure.feature("Логин пользователя")
class TestLogin:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self, api, registered_user):
        with allure.step("Логинимся под существующим пользователем"):
            response = api.login(
                {
                    "email": registered_user["email"],
                    "password": registered_user["password"],
                }
            )

        body = response.json()

        assert response.status_code == 200
        assert body.get("success") is True
        assert "accessToken" in body
        assert "refreshToken" in body

    @allure.title("Вход с неверным логином и паролем")
    def test_login_wrong_credentials(self, api):
        with allure.step("Логинимся с неверными данными"):
            response = api.login(
                {
                    "email": "nope@yandex.ru",
                    "password": "wrong",
                }
            )

        body = response.json()

        assert response.status_code == 401
        assert body.get("success") is False