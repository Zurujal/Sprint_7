import allure
import requests
import data


class TestDeleteCourier:

    @allure.title("Проверяем удаление курьера c валидным id")
    def test_delete_courier_valid_id(self):
        requests.post(f'{data.BASE_URL}{data.CREATE_COURIER_ENDPOINT}', data=data.COURIER)
        login = requests.post(f'{data.BASE_URL}{data.LOGIN_COURIER_ENDPOINT}', data=data.COURIER)
        result = requests.delete(f'{data.BASE_URL}{data.DELETE_COURIER_ENDPOINT}{login.json()["id"]}')
        assert result.status_code == 200 and result.json()["ok"] is True

    @allure.title("Проверяем удаление курьера без id")
    def test_delete_courier_without_id(self):
        result = requests.delete(f'{data.BASE_URL}{data.DELETE_COURIER_ENDPOINT}')
        assert result.status_code == 404 and result.json()["message"] == "Not Found."

    @allure.title("Проверяем удаление курьера c несуществующим id")
    def test_delete_courier_without_id(self):
        result = requests.delete(f'{data.BASE_URL}{data.DELETE_COURIER_ENDPOINT}-1')
        assert result.status_code == 404 and result.json()["message"] == "Курьера с таким id нет."
