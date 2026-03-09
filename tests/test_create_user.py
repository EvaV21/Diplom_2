import allure

from src.helpers import generate_user


@allure.epic("Создание пользователя")
class TestCreateUser:

    @allure.title("Можно создать уникального пользователя")
    def test_create_unique_user_success(self, api, cleanup_user):
        user = generate_user()

        with allure.step("Регистрируем уникального пользователя"):
            response = api.register(user)

        body = response.json()

        if response.status_code == 200 and "accessToken" in body:
            cleanup_user.append(body["accessToken"])

        assert response.status_code == 200
        assert body.get("success") is True
        assert "accessToken" in body
        assert "refreshToken" in body
        assert body["user"]["email"] == user["email"]
        assert body["user"]["name"] == user["name"]

    @allure.title("Нельзя создать двух одинаковых пользователей")
    def test_create_duplicate_user_returns_error(self, api, cleanup_user):
        user = generate_user()

        with allure.step("Регистрируем пользователя впервые"):
            first_response = api.register(user)

        first_body = first_response.json()

        if first_response.status_code == 200 and "accessToken" in first_body:
            cleanup_user.append(first_body["accessToken"])

        with allure.step("Повторно отправляем запрос на регистрацию того же пользователя"):
            response = api.register(user)

        body = response.json()

        assert response.status_code == 403
        assert body.get("success") is False
        assert body.get("message") == "User already exists"

    @allure.title("Нельзя создать пользователя без обязательного поля")
    def test_create_user_without_required_field_returns_error(self, api, cleanup_user):
        user = generate_user()
        user.pop("name")

        with allure.step("Отправляем запрос на регистрацию без поля name"):
            response = api.register(user)

        body = response.json()

        if response.status_code == 200 and "accessToken" in body:
            cleanup_user.append(body["accessToken"])

        assert response.status_code == 403
        assert body.get("success") is False
        assert body.get("message") == "Email, password and name are required fields"