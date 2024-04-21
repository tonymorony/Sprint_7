import allure
from api.order_api import OrderApi


class TestOrdersList:
    @allure.title('Успешное получение списка заказов')
    def test_get_order_list_success(self):
        order_api = OrderApi()
        response = order_api.get_orders_list()
        assert response.status_code == 200 and "orders" in response.json()
