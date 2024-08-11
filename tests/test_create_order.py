import allure
import requests
import data
import pytest


class TestCreateOrder:

    @allure.title("Проверка успешного создания заказа")
    @pytest.mark.parametrize(
        "payload", (data.ORDER_BLACK_PAYLOAD, data.ORDER_GREY_PAYLOAD, data.ORDER_BOTH_COLORS_PAYLOAD,
                    data.ORDER_EMPTY_COLOR_PAYLOAD)
    )
    def test_create_order(self, payload):
        result = requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_ENDPOINT}', json=payload)
        assert result.status_code == 201 and result.json()["track"] > 0
