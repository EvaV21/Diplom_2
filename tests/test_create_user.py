import allure

from src.helpers import generate_user


@allure.epic("Создание пользователя")
class TestCreateUser:

    @allure.title("Можно создать уникального пользователя")
    def test_create_unique_user_success(self, registered_user):
        response = registered_user["response"]
        body = response.json()

        assert response.status_code == 200
        assert body.get("success") is True
        assert "accessToken" in body
        assert "refreshToken" in body
        assert body["user"]["email"] == registered_user["email"]
        assert body["user"]["name"] == registered_user["name"]

    @allure.title("Нельзя создать двух одинаковых пользователей")
    def test_create_duplicate_user_returns_error(self, api, registered_user):
        payload = {
            "email": registered_user["email"],
            "password": registered_user["password"],
            "name": registered_user["name"],
        }

        with allure.step("Повторно отправляем запрос на регистрацию того же пользователя"):
            response = api.register(payload)

        body = response.json()

        assert response.status_code == 403
        assert body.get("success") is False
        assert body.get("message") == "User already exists"

    @allure.title("Нельзя создать пользователя без обязательного поля")
    def test_create_user_without_required_field_returns_error(self, api):
        user = generate_user()
        user.pop("name")

        with allure.step("Отправляем запрос на регистрацию без поля name"):
            response = api.register(user)

        body = response.json()

        assert response.status_code == 403
        assert body.get("success") is False
        assert body.get("message") == "Email, password and name are required fields"