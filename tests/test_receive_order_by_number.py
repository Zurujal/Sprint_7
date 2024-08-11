import requests
import data
import allure


class TestLoginCourier:
    @allure.title("Проверка успешного получения заказа по номеру")
    def test_get_order(self):
        create_order = requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_ENDPOINT}',
                                     json=data.ORDER_BOTH_COLORS_PAYLOAD)
        get_order = requests.get(f'{data.BASE_URL}{data.GET_ORDER_ENDPOINT}?t={create_order.json()["track"]}')
        assert get_order.status_code == 200 and get_order.json()["order"]["firstName"] == "Naruto"

    @allure.title("Проверка получения заказа по номеру без track id в запросе")
    def test_get_order_without_track(self):
        get_order = requests.get(f'{data.BASE_URL}{data.GET_ORDER_ENDPOINT}')
        assert get_order.status_code == 400 and get_order.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Проверка получения заказа по номеру с некорректным track id в запросе")
    def test_get_order_with_invalid_track(self):
        get_order = requests.get(f'{data.BASE_URL}{data.GET_ORDER_ENDPOINT}?t=01')
        assert get_order.status_code == 404 and get_order.json()["message"] == "Заказ не найден"