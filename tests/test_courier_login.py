import allure
from api.courier_api import CourierApi
from data import TestsData as TD


class TestCourierLogin:
    @allure.title('Проверка успешной авторизации')
    def test_login_success(self):
        courier_api = CourierApi()
        response = courier_api.login_courier(TD.LOGIN_SUCCESS_DATASET)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title('Авторизация несуществующего пользователя')
    def test_login_non_existent_user(self):
        courier_api = CourierApi()

        response = courier_api.login_courier(TD.NON_EXISTING_COURIER_DATASET)
        assert response.status_code == 404 and response.json()['message'] == TD.ACCOUNT_NOT_FOUND_ERROR

    @allure.title('Авторизация без ввода логина')
    def test_login_without_login_failure(self):
        courier_api = CourierApi()
        response = courier_api.login_courier(TD.NO_LOGIN_DATASET)
        assert response.status_code == 400 and response.json()['message'] == TD.LOGIN_MISSING_DATA_ERROR

    @allure.title('Авторизация без ввода пароля')
    def test_login_without_password_failure(self):
        courier_api = CourierApi()
        response = courier_api.login_courier(TD.NO_PASSWORD_DATASET)
        assert response.status_code == 400 and response.json()['message'] == TD.LOGIN_MISSING_DATA_ERROR

    @allure.title('Авторизация без логина и пароля')
    def test_login_without_login_and_password_failure(self):
        courier_api = CourierApi()
        response = courier_api.login_courier(TD.NO_LOGIN_AND_PASSWORD_DATASET)
        assert response.status_code == 400 and response.json()['message'] == TD.LOGIN_MISSING_DATA_ERROR
