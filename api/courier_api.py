import allure
import requests
from data import TestsData as TD


class CourierApi:
    def __init__(self):
        self.courier_id = None

    @allure.step('Создание курьера')
    def create_courier(self, data):
        return requests.post(TD.COURIER_CREATION_ENDPOINT, data=data)

    @allure.step('Логин курьера')
    def login_courier(self, data):
        response = requests.post(TD.COURIER_LOGIN_ENDPOINT, data=data)
        if response.status_code == 200:
            self.courier_id = response.json().get("id")
        return response
