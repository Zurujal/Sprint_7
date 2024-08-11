BASE_URL = "https://qa-scooter.praktikum-services.ru/"
CREATE_COURIER_ENDPOINT = "api/v1/courier"
LOGIN_COURIER_ENDPOINT = "api/v1/courier/login"
CREATE_ORDER_ENDPOINT = "api/v1/orders"
GET_ORDER_LIST_ENDPOINT = "api/v1/orders"
DELETE_COURIER_ENDPOINT = "api/v1/courier/"
ACCEPT_ORDER_ENDPOINT = "api/v1/orders/accept/"
GET_ORDER_ENDPOINT = "api/v1/orders/track"
ONLY_LOGIN = {"login": "zurujal", "password": "", "firstName": ""}
ONLY_PASSWORD = {"login": "", "password": "12345", "firstName": ""}
ONLY_NAME = {"login": "", "password": "", "firstName": "Sergey"}
COURIER = {"login": "ZurujalTempCourier", "password": "12345"}
WRONG_PASSWORD = {"login": "zurujal", "password": "54321", "firstName": "Sergey"}
WRONG_LOGIN = {"login": "lajuruz", "password": "12345", "firstName": "Sergey"}
ORDER_BLACK_PAYLOAD = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
ORDER_GREY_PAYLOAD = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "GREY"
    ]
}
ORDER_BOTH_COLORS_PAYLOAD = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK",
        "GREY"
    ]
}
ORDER_EMPTY_COLOR_PAYLOAD = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}
