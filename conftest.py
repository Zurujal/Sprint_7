import pytest
import requests
import data

@pytest.fixture()
def courier_for_test():
    create = requests.post(f'{data.BASE_URL}{data.CREATE_COURIER_ENDPOINT}', data=data.COURIER)
    yield create
    login = requests.post(f'{data.BASE_URL}{data.LOGIN_COURIER_ENDPOINT}', data=data.COURIER)
    requests.delete(f'{data.BASE_URL}{data.DELETE_COURIER_ENDPOINT}{login.json()["id"]}')
