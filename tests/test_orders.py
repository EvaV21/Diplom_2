import allure


@allure.feature("Создание заказа")
class TestOrders:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, api, token, ingredient_ids):
        r = api.create_order(ingredients=ingredient_ids, token=token)
        assert r.status_code == 200
        body = r.json()

        assert body.get("success") is True
        assert "order" in body
        assert "number" in body["order"]

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, api, ingredient_ids):
        r = api.create_order(ingredients=ingredient_ids, token=None)
        assert r.status_code == 200
        body = r.json()

        assert body.get("success") is True
        assert "order" in body
        assert "number" in body["order"]

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, api, ingredient_ids):
        r = api.create_order(ingredients=ingredient_ids, token=None)
        assert r.status_code == 200
        body = r.json()

        assert body.get("success") is True
        assert "order" in body
        assert "number" in body["order"]

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, api):
        r = api.create_order(ingredients=[])
        assert r.status_code == 400
        body = r.json()

        assert body.get("success") is False

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_hash(self, api):
        r = api.create_order(ingredients=["invalid_hash"])
        assert r.status_code == 400
        body = r.json()
        assert body.get("success") is False