import allure
import requests
from data import TestsData as TD


class OrderApi:
    @allure.step('Создаем новый заказ')
    def create_order(self, data):
        return requests.post(TD.ORDERS_ENDPOINT, json=data)

    @allure.step('Получаем список заказов')
    def get_orders_list(self):
        return requests.get(TD.ORDERS_ENDPOINT)
