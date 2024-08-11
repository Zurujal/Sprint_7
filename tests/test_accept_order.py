import allure
import requests
import data


class TestAcceptOrder:

    @allure.title("Проверяем возможность принять заказ")
    def test_accept_order(self, courier_for_test):
        login = requests.post(f'{data.BASE_URL}{data.LOGIN_COURIER_ENDPOINT}', data=data.COURIER)
        create_order = requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_ENDPOINT}',
                                     json=data.ORDER_BOTH_COLORS_PAYLOAD)
        get_order = requests.get(f'{data.BASE_URL}{data.GET_ORDER_ENDPOINT}?t={create_order.json()["track"]}')
        accept_order = requests.put(f'{data.BASE_URL}{data.ACCEPT_ORDER_ENDPOINT}{get_order.json()["order"]["id"]}'
                                    f'?courierId={login.json()["id"]}')
        assert accept_order.status_code == 200 and accept_order.json()["ok"] is True

    @allure.title("Проверяем принятие заказа без id курьера в запросе")
    def test_accept_order_without_courier_id(self):
        create_order = requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_ENDPOINT}',
                                     json=data.ORDER_BOTH_COLORS_PAYLOAD)
        get_order = requests.get(f'{data.BASE_URL}{data.GET_ORDER_ENDPOINT}?t={create_order.json()["track"]}')
        accept_order = requests.put(f'{data.BASE_URL}{data.ACCEPT_ORDER_ENDPOINT}{get_order.json()["order"]["id"]}')
        assert accept_order.status_code == 400 and accept_order.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Проверяем принятие заказа c некорректным id курьера в запросе")
    def test_accept_order_with_invalid_courier_id(self):
        create_order = requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_ENDPOINT}',
                                     json=data.ORDER_BOTH_COLORS_PAYLOAD)
        get_order = requests.get(f'{data.BASE_URL}{data.GET_ORDER_ENDPOINT}?t={create_order.json()["track"]}')
        accept_order = requests.put(f'{data.BASE_URL}{data.ACCEPT_ORDER_ENDPOINT}{get_order.json()["order"]["id"]}'
                                    f'?courierId=-1')
        assert accept_order.status_code == 404 and accept_order.json()["message"] == "Курьера с таким id не существует"

    @allure.title("Проверяем принятие заказа без id заказа в запросе")
    def test_accept_order_without_order_id(self, courier_for_test):
        login = requests.post(f'{data.BASE_URL}{data.LOGIN_COURIER_ENDPOINT}', data=data.COURIER)
        accept_order = requests.put(f'{data.BASE_URL}{data.ACCEPT_ORDER_ENDPOINT}courierId={login.json()["id"]}')
        assert accept_order.status_code == 400 and accept_order.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Проверяем принятие заказа c некорректным id заказа в запросе")
    def test_accept_order_with_invalid_order_id(self, courier_for_test):
        login = requests.post(f'{data.BASE_URL}{data.LOGIN_COURIER_ENDPOINT}', data=data.COURIER)
        accept_order = requests.put(f'{data.BASE_URL}{data.ACCEPT_ORDER_ENDPOINT}-1?courierId={login.json()["id"]}')
        assert accept_order.status_code == 404 and accept_order.json()["message"] == "Заказа с таким id не существует"
