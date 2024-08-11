import requests
import data
import pytest
import allure


class TestLoginCourier:
    @allure.title("Проверка успешного логина курьера")
    def test_login_courier(self,courier_for_test):
        result = requests.post(f'{data.BASE_URL}{data.LOGIN_COURIER_ENDPOINT}', data=data.COURIER)
        assert result.status_code == 200 and result.json()["id"] == result.json()["id"]

    @allure.title("Проверка невозможности логина курьера если не заполнены все обязательные поля")
    @pytest.mark.parametrize("payload", (data.ONLY_LOGIN, data.ONLY_PASSWORD))
    def test_unable_to_login_without_required_data(self, payload):
        result = requests.post(f'{data.BASE_URL}{data.LOGIN_COURIER_ENDPOINT}', data=payload)
        assert result.status_code == 400 and result.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Проверка невозможности логина курьера если пароль или логин некорректные")
    @pytest.mark.parametrize("payload", (data.WRONG_LOGIN, data.WRONG_PASSWORD))
    def test_unable_to_login_with_wrong_data(self, payload):
        result = requests.post(f'{data.BASE_URL}{data.LOGIN_COURIER_ENDPOINT}', data=payload)
        assert result.status_code == 404 and result.json()["message"] == "Учетная запись не найдена"
