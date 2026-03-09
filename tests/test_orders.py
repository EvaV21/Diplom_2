import allure


@allure.epic("Создание заказа")
class TestOrders:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, api, token, ingredient_ids):
        response = api.create_order(
            ingredients=ingredient_ids["ids"],
            token=token["access_token"]
        )

        body = response.json()

        assert response.status_code == 200
        assert body.get("success") is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, api, ingredient_ids):
        response = api.create_order(
            ingredients=ingredient_ids["ids"],
            token=None
        )

        body = response.json()

        assert response.status_code == 200
        assert body.get("success") is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, api, ingredient_ids):
        response = api.create_order(
            ingredients=ingredient_ids["ids"],
            token=None
        )

        body = response.json()

        assert response.status_code == 200
        assert body.get("success") is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, api):
        response = api.create_order()

        body = response.json()

        assert response.status_code == 400
        assert body.get("success") is False

    @allure.title("Создание заказа с неверным хешем")
    def test_create_order_with_invalid_hash(self, api):
        response = api.create_order(
            ingredients=["invalid_hash"]
        )

        body = response.json()

        assert response.status_code == 400
        assert body.get("success") is False