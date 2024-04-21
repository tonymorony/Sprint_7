import allure
import utils
from data import TestsData as TD
from api.courier_api import CourierApi


class TestCourierCreation:

    @allure.title('Проверка успешного создания курьера c валидными данными')
    def test_courier_creation_valid_data_success(self):
        courier_api = CourierApi()
        new_courier_data = utils.courier_data_generation()
        creation_response = courier_api.create_courier(new_courier_data)
        assert creation_response.status_code == 201 and creation_response.json()['ok']

    @allure.title('Проверка невозможности создания одинаковых курьеров')
    def test_courier_creation_same_data_failure(self):
        courier_api = CourierApi()
        new_courier_data = utils.courier_data_generation()
        creation_response = courier_api.create_courier(new_courier_data)
        assert creation_response.status_code == 201 and creation_response.json()['ok']
        creation_response = courier_api.create_courier(new_courier_data)
        assert creation_response.status_code == 409 and creation_response.json()['message'] == TD.TAKEN_LOGIN_ERROR

    @allure.title('Проверка невозможности создания курьера с пустым логином')
    def test_courier_creation_empty_login_failure(self):
        courier_api = CourierApi()
        new_courier_data = utils.courier_data_generation()
        new_courier_data['login'] = ''
        creation_response = courier_api.create_courier(new_courier_data)
        assert creation_response.status_code == 400 and creation_response.json()['message'] == TD.MISSING_DATA_ERROR

    @allure.title('Проверка невозможности создания курьера с пустым паролем')
    def test_courier_creation_empty_password_failure(self):
        courier_api = CourierApi()
        new_courier_data = utils.courier_data_generation()
        new_courier_data['password'] = ''
        creation_response = courier_api.create_courier(new_courier_data)
        assert creation_response.status_code == 400 and creation_response.json()['message'] == TD.MISSING_DATA_ERROR

    @allure.title('Проверка невозможности создания курьера с существующим логином')
    def test_courier_creation_taken_login_failure(self):
        courier_api = CourierApi()
        new_courier_data = utils.courier_data_generation()
        creation_response = courier_api.create_courier(new_courier_data)
        assert creation_response.status_code == 201 and creation_response.json()['ok']
        new_courier_data['password'] = utils.courier_data_generation()['password']
        new_courier_data['name'] = utils.courier_data_generation()['name']
        creation_response = courier_api.create_courier(new_courier_data)
        assert creation_response.status_code == 409 and creation_response.json()['message'] == TD.TAKEN_LOGIN_ERROR
