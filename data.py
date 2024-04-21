class TestsData:
    SERVICE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_CREATION_ENDPOINT = SERVICE_URL + '/api/v1/courier'
    COURIER_LOGIN_ENDPOINT = SERVICE_URL + '/api/v1/courier/login'
    ORDERS_ENDPOINT = SERVICE_URL + '/api/v1/orders'
    TAKEN_LOGIN_ERROR = 'Этот логин уже используется. Попробуйте другой.'
    MISSING_DATA_ERROR = 'Недостаточно данных для создания учетной записи'
    LOGIN_MISSING_DATA_ERROR = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND_ERROR = 'Учетная запись не найдена'
    LOGIN_SUCCESS_DATASET = {
        "login": "tonyl",
        "password": "12345"
    }
    NON_EXISTING_COURIER_DATASET = {
            "login": "tonyl12312312312312321",
            "password": "12345"
        }
    NO_LOGIN_DATASET = {
            "login": "",
            "password": "12345"
        }
    NO_PASSWORD_DATASET = {
            "login": "12345",
            "password": ""
        }
    NO_LOGIN_AND_PASSWORD_DATASET = {
        "login": "",
        "password": ""
    }
    ORDER_TEST_DATASET = {
            "firstName": "Tony",
            "lastName": "L",
            "address": "Pushkina str. Kolotushkina 5",
            "metroStation": "1",
            "phone": "+71234561234",
            "rentTime": 2,
            "deliveryDate": "2024-04-21",
            "comment": "Faster!",
        }