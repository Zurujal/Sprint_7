import allure
import requests
import data


class TestCreateCourier:
    @allure.title("Проверка успешного создания курьера")
    def test_create_courier(self, courier_for_test):
        assert courier_for_test.status_code == 201 and courier_for_test.json()["ok"] is True

    @allure.title("Проверка невозможности создания курьера с существующим логином")
    def test_unable_to_create_similar_couriers(self, courier_for_test):
        result = requests.post(f'{data.BASE_URL}{data.CREATE_COURIER_ENDPOINT}', data=data.COURIER)
        assert result.status_code == 409 and result.json()[
            "message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Проверка невозможности создания курьера если не заполнены все обязательные поля")
    def test_unable_to_create_courier_without_required_data(self):
        result = requests.post(f'{data.BASE_URL}{data.CREATE_COURIER_ENDPOINT}', data=data.ONLY_LOGIN)
        assert result.status_code == 400 and result.json()["message"] == ("Недостаточно данных для создания учетной "
                                                                          "записи")
