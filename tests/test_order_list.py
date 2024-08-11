import allure
import requests

import data


class TestOrderList:

    @allure.title("Проверяем что тело ответа содержит список заказов")
    def test_order_list(self):
        order = requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_ENDPOINT}', json=data.ORDER_BOTH_COLORS_PAYLOAD)
        result = requests.get(f'{data.BASE_URL}{data.GET_ORDER_LIST_ENDPOINT}/track?t={order.json()["track"]}')
        assert result.status_code == 200 and result.json()["order"]["firstName"] == "Naruto"
